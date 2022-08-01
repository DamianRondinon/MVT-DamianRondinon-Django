from django.shortcuts import render
from django.http import HttpResponse
from coder.models import Familiares
from django.template import Template, Context, loader

# Create your views here.
def lista_familiares(request):

    familia = Familiares.objects.all()

    template = loader.get_template("familia.html")

    info = {"familia":familia}

    template = loader.get_template("familia.html")

    documento = template.render(info)


    return HttpResponse(documento)


    

    