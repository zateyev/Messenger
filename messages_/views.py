from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils.translation import ugettext as _

from messages_.forms import SignUpForm, MessageForm
from messages_.models import Message
from registrar.models import Registrar


def index(request):
    return render(request, 'base.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # binding data to the form
        if form.is_valid():
            registrar = Registrar()
            code = registrar.generate_code()
            request.session['code'] = code
            request.session['form'] = {'phone': form.cleaned_data['phone'], 'password': form.cleaned_data['password']}
            return render(request, 'confirm.html', {})
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'signup.html', {'form': SignUpForm()})


def confirm(request):
    form = request.session.get('form')
    if str(request.session.get('code')) == str(request.POST.get('code')):
        if Registrar.register(form['phone'], form['password']):
            return render(request, 'login.html', {'confirmation': _('Your account has been created')})
        else:
            return HttpResponse("User with phone %s is already in use" % form['phone'])
    else:
        return HttpResponse(loader.get_template('confirm.html').render(request))


def profile(request):
    template = loader.get_template('accounts/profile.html')
    return HttpResponse(template.render({'request': request}, request))


def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)  # binding data to the form
        if form.is_valid():
            text = form.cleaned_data['text']
            receiver = get_object_or_404(User, username=form.cleaned_data['receiver'])
            Message.objects.create(text=text, sender=request.user, receiver=receiver)
            return redirect('sent')
        else:
            return render(request, 'accounts/new_message.html', {'form': form})
    else:
        return render(request, 'accounts/new_message.html', {'form': MessageForm()})


def add_to_favorites(request):
    message_id = request.POST.get('message_id')
    message = get_object_or_404(Message, pk=message_id)
    message.state = 4
    message.save()
    return redirect('view_favorites')


def delete_from_inbox(request):
    message_id = request.POST.get('message_id')
    request.user.inbox.filter(pk=message_id).delete()
    return redirect('inbox')


def delete_from_sent(request):
    message_id = request.POST.get('message_id')
    request.user.outbox.filter(pk=message_id).delete()
    return redirect('sent')


def delete_from_starred(request):
    message_id = request.POST.get('message_id')
    message = get_object_or_404(Message, pk=message_id)
    message.state = 3
    message.save()
    return redirect('view_favorites')


def view_favorites(request):
    context = {'favorite_messages': request.user.inbox.filter(state=4).order_by('-timestamp')}
    return render(request, 'accounts/favorite_messages.html', context)


def view_inbox(request):
    context = {'messages': request.user.inbox.all().order_by('-timestamp')}
    return render(request, 'accounts/inbox.html', context)


def view_sent(request):
    context = {'messages': request.user.outbox.all().order_by('-timestamp')}
    return render(request, 'accounts/sent.html', context)


def read_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.state = 3
    message.save()
    return redirect('inbox')
