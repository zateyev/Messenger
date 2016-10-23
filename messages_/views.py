from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from messages_.forms import SignUpForm, MessageForm
from messages_.models import Message
from registrar.models import Registrar


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))


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
            return render(request, 'base.html', {})
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
            return redirect('sent')
        else:
            return render(request, 'accounts/new_message.html', {'form': form})
    else:
        return render(request, 'accounts/new_message.html', {'form': MessageForm()})


def view_inbox(request):
    context = {'messages': Message.objects.all().filter(receiver=request.user)}
    return render(request, 'accounts/inbox.html', context)


def view_sent(request):
    context = {'messages': Message.objects.all().filter(sender=request.user)}
    return render(request, 'accounts/sent.html', context)
