from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import AddProjectForm
# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView

from App.forms import AddProjectForm
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

def AddProject(request):
        if request.method == "GET":
            form = AddProjectForm()
            return render(request,'App/AddProject.html',
                          {'f': form})

        if request.method == "POST":
            form = AddProjectForm(request.POST)
            if form.is_valid():
                result = form.save() #result = form.save(commit = False)
                result.save()
                return HttpResponseRedirect(reverse('displayy'))

            else:
                return render(request, 'App/AddProject.html',
                              {'f': form,
                               'msg_error': "Could not add a new project."})

class AddP(CreateView):
    model = Projet
    fields = ('nom_projet', 'createur', 'superviseur', 'duree_projet', 'temps_alloue_par_projet',
              'besoins', 'description', 'est_valide')
    success_url =  reverse_lazy('displayy')
    #template_name = "AddProject.html"


def DeleteProject(request,id):
    #request.POST['id']
    project = Projet.objects.get(pk=id)
    project.delete()
    return HttpResponseRedirect(reverse('disp'))

class DeleteP(DeleteView):
    model = Projet
    success_url = reverse_lazy('disp')


def loginuser(request):
    if request.method == "POST":
        u = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(request, username= u, password= pwd)
        if user is not None:
            login(request,user)
            return redirect('disp')
        else:
            messages.info(request, 'username or passsword not valid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')

def registeruser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
            form = UserCreationForm()
    return render(request, 'register.html', {'f':form})


def home(request):
    return render(request, 'base.html')
