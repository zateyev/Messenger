from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from messages_.models import Message
from registrar.models import Registrar


def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))


def signup(request):
    return render(request, 'signup.html', {})


def register(request):
    registrar = Registrar()
    code = registrar.generate_code()
    request.session['code'] = code
    form = {}
    if request.POST:
        form['phone'] = request.POST.get('phone')
        form['password'] = request.POST.get('password')
    request.session['form'] = form
    return render(request, 'confirm.html', {})


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
    return render(request, 'accounts/new_message.html', {})


def write_message(request):
    receiver = text = ''
    if request.POST:
        receiver = request.POST.get('receiver')
        text = request.POST.get('text')
    receiver = User.objects.filter(username=receiver)[0]
    message = Message.create(text, request.user, receiver)
    message.save()
    return HttpResponse("Your message has been sent")


def view_inbox(request):
    context = {'messages': Message.objects.all().filter(receiver=request.user)}
    return render(request, 'accounts/inbox.html', context)


def view_sent(request):
    context = {'messages': Message.objects.all().filter(sender=request.user)}
    return render(request, 'accounts/sent.html', context)
