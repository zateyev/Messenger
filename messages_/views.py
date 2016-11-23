from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from messages_.forms import SignUpForm, MessageForm
from messages_.models import Message, Account
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
            return render(request, 'login.html', {'confirmation': 'Your account has been created'})
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
            receiver = form.cleaned_data['receiver']
            text = form.cleaned_data['text']
            receiver = User.objects.filter(username=receiver)[0]
            message = Message.create(text, request.user, receiver)
            message.save()
            sender_account = Account.objects.get(user=request.user)
            sender_account.sent.add(message)
            receiver_account = Account.objects.get(user=receiver)
            receiver_account.inbox.add(message)
            return redirect('sent')
        else:
            return render(request, 'accounts/new_message.html', {'form': form})
    else:
        return render(request, 'accounts/new_message.html', {'form': MessageForm()})


def add_to_favorites(request):
    message_id = request.POST.get('message_id')
    message = Message.objects.get(pk=message_id)
    account = Account.objects.get(user=request.user)
    account.starred.add(message)
    return redirect('view_favorites')


def delete_from_inbox(request):
    message_id = request.POST.get('message_id')
    message = Message.objects.get(pk=message_id)
    account = Account.objects.get(user=request.user)
    account.inbox.remove(message)
    return redirect('inbox')


def delete_from_sent(request):
    message_id = request.POST.get('message_id')
    message = Message.objects.get(pk=message_id)
    account = Account.objects.get(user=request.user)
    account.sent.remove(message)
    return redirect('sent')


def delete_from_starred(request):
    message_id = request.POST.get('message_id')
    message = Message.objects.get(pk=message_id)
    account = Account.objects.get(user=request.user)
    account.starred.remove(message)
    return redirect('view_favorites')


def view_favorites(request):
    account = Account.objects.get(user=request.user)
    context = {'favorite_messages': account.starred.order_by('-timestamp')}
    return render(request, 'accounts/favorite_messages.html', context)


def view_inbox(request):
    account = Account.objects.get(user=request.user)
    context = {'messages': account.inbox.order_by('-timestamp')}
    return render(request, 'accounts/inbox.html', context)


def view_sent(request):
    account = Account.objects.get(user=request.user)
    context = {'messages': account.sent.order_by('-timestamp')}
    return render(request, 'accounts/sent.html', context)


def read_message(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.state = 3
    message.save()
    return redirect('inbox')
