from django.urls import path
from .views import *
urlpatterns=[
    path('',Listview,name='tracks'),
    path('Add',Addview,name='tracknew'),
    path('Update/<int:id>',Updateview,name='trackupdate'),
    path('Delete/<int:id>',Deleteview,name='trackdelete'),
    path('<str:name>',findview,name='trackfind'),
]