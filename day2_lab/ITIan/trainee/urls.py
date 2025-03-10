from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    # path('login/', login, name="login"),
    # path('delete/<int:trainee_id>', delete_trainee, name="delete"),
    # path('add/', add_trainee, name="add"),
    # path('update', update_trainee, name="update"),
    path('trainee_list/', trainee_list, name="trainee_list"),
    # path('show/', show, name="show"),
]
# mapping the images/ to media root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)