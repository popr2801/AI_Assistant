from django.urls import path, include
from .views import index,assistant,login,register,dashboard,delete_file

urlpatterns = [
    path('',index),
    path('assistant/',assistant,name='assistant'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete/<int:id>/',delete_file, name='delete_file')
]