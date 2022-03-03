from django.urls import path, include

from . import views
from .views import Display2, AddP, DeleteP

urlpatterns = [
    path('a/', views.index),
    # path('index/<int:classe>', views.index_param),
    path('index/<name>', views.index_param),
    path('index_template', views.index_template),
    path('display', views.Display, name="disp"),
    path('displaytable', Display2.as_view(), name='displayy'),
    path('add/', views.AddProject, name='addadd'),
    path('addproject/', views.AddP.as_view(), name='addd'),
    #path('delete1/<int:id>', views.DeleteProject, name='dd'),
    path('delete/<int:pk>', views.DeleteP.as_view(), name='dl'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
    path('home/', views.home, name='home'),


]
