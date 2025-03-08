from django.urls import path
from .views import *
urlpatterns=[
path('Login/',Loginview,name='Login'),
    path('Logout/',logoutview,name='Logout'),
    path('Reg/',Regview,name='Reg'),
]