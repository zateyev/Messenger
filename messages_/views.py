from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from registrar.models import Registrar


@csrf_protect
def index(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render(request))


@csrf_protect
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(request))


@csrf_protect
def register(request):
    template = loader.get_template('confirm.html')
    registrar = Registrar()
    code = registrar.generate_code()
    request.session['code'] = code
    form = {}
    if request.POST:
        form['phone'] = request.POST.get('phone')
        form['password'] = request.POST.get('password')
    request.session['form'] = form
    return HttpResponse(template.render(request))
    # return render(request, 'confirm.html', {})


@csrf_protect
def confirm(request):
    form = request.session.get('form')
    if str(request.session.get('code')) == str(request.POST.get('code')):
        if Registrar.register(form['phone'], form['password']):
            return HttpResponse("Thank you, your account has been created!")
        else:
            return HttpResponse("User with phone %s is already in use" % form['phone'])
    else:
        return HttpResponse(loader.get_template('confirm.html').render(request))


def profile(request):
    template = loader.get_template('accounts/profile.html')
    return HttpResponse(template.render({'request': request}, request))
