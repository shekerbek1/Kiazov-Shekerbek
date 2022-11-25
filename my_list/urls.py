from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('mane/', views.mane, name='mane'),
    path('create/', views.create, name='create')

 ]