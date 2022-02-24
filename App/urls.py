from django.urls import path, include

from . import views
from .views import Display2, AddP

urlpatterns = [
    path('a/', views.index),
    # path('index/<int:classe>', views.index_param),
    path('index/<name>', views.index_param),
    path('index_template', views.index_template),
    path('displaytable', views.Display),
    path('display', Display2.as_view(), name = 'displayy'),
    path('add/', views.AddProject, name='addadd'),
    path('addproject/', views.AddP.as_view(), name='addd'),


]
