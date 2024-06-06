from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people', views.people, name='people'),
]