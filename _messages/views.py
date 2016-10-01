from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from registrar.models import Registrar
from .models import *


@csrf_exempt
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


@csrf_exempt
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


@csrf_exempt
def confirm(request):
    form = request.session.get('form')
    if str(request.session.get('code')) == str(request.POST.get('code')):
        Registrar.register(form['phone'], form['password'])
        return HttpResponse("Thank you, your account has been created!")
    return HttpResponse("Oops, something went wrong!")

