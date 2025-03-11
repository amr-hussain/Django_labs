from django.urls import path
from .views import *
urlpatterns = [

    path('', course_list, name="show"),
    # path('add/', add_course, name="add"),
    # path('update/<int:course_id>', update_course, name="update"),
    # path('delete/<int:course_id>', delete_course, name="delete"),

    ]