from django.urls import path
from .views import *
urlpatterns = [

    path('login/', login, name="login"),
    path('delete/<int:trainee_id>', delete_trainee, name="delete"),
    path('add/', add_trainee, name="add"),
    path('update', update_trainee, name="update"),
    path('trainees/', list_trainees, name="show"),
    path('show/', show, name="show"),
]