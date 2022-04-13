from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from httplib2 import Http
from .models import User
from django.urls import reverse

def index(request):
  template = loader.get_template('index.html')
  users = User.objects.all().values()
  context = {
    'users': users,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  firstname = request.POST['nom']
  lastname = request.POST['prenom']
  email = request.POST['mail']
  dat = request.POST['date_naiss']
  tel = request.POST['phone']

  user = User(nom=firstname, prenom=lastname, mail=email, date_naiss=dat, phone=tel)
  user.save()
  return HttpResponseRedirect(reverse('index'))
