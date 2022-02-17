from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


from App.models import Projet


def index(request):
    return HttpResponse('hi')

def index_param(request,name):
    return HttpResponse('hi '+ name)
    #return HttpResponse('hi '+ str(classe))

def index_template(request):
    return render(request,'App/index.html')

def Display(request):
    project= Projet.objects.all()
    #result='--'.join(p.nom_projet for p in project)
    #return HttpResponse(result)
    return render(request,'App/display.html',
                  {'pp':project})

class Display2(ListView):
    model=Projet
    template_name ='App/display.html'
    context_object_name = 'pp'

