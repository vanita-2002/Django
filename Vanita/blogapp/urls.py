from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('home/',views.home),
    path('about/',views.about),
    path('create/',views.create,name='create'),
    path('insert/',views.insert,name='add'),
    path('edit/<pk>',views.edit,name='edit'),
      path('update',views.update,name='update'),



]
