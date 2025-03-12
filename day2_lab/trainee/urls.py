from django.urls import path, include
from .views import *



urlpatterns = [
    path('', trainee_list, name="main"),
    path('add', trainee_add, name="add"),
    path('update/<int:trainee_id>', trainee_update, name="update"),
    path('delete/<int:trainee_id>', trainee_delete, name="delete"),
    
]
