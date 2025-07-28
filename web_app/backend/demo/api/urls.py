from django.urls import path, include
from .views import index,uploadFile,login

urlpatterns = [
    path('',index),
    path('upload/',uploadFile,name='uploadFile'),
    path('login/',login,name='login')
]