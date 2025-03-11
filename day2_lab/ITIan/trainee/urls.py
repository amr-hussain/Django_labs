from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', trainee_list, name="main"),
    path('add', trainee_add, name="add"),
    path('update/<int:trainee_id>', trainee_update, name="update"),
    path('delete/<int:trainee_id>', trainee_delete, name="delete"),
    

]
# mapping the images/ to media root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)