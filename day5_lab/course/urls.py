from django.urls import path
from .views import *
urlpatterns = [

    path('', course_list, name="list"),
    path('add/', add_course, name="add"),
    path('update/<int:course_id>', update_course, name="update"),
    path('delete/<int:course_id>', delete_course, name="delete"),
    # path('course/add/', add_course, name='add_new_course'),
    ]