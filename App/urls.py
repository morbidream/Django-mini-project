from django.urls import path, include

from . import views
from .views import Display2

urlpatterns = [
    path('a/', views.index),
    path('index/<name>', views.index_param),
    path('index_template', views.index_template),
    path('displaytable', views.Display),
    path('display', Display2.as_view()),
    #path('index/<int:classe>', views.index_param),

]
