from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
   

    path('', TraineeList.as_view(), name="main"),
    path('add', TraineeAdd.as_view(), name="add_trainee"),
    path('update/<pk>', TraineeUpdate.as_view(), name="update_trainee"),
    path('delete/<pk>', TraineeDelete.as_view(), name="delete_trainee"),
    path('logout', Logout.as_view(), name="logout"),
    path('login/', Login.as_view(), name="login"),
    path('signup', Signup.as_view(), name="signup"),
    path('api/', TraineeLC.as_view(), name='apiLC'),
    # path('api', TraineeListCreateView.as_view(), name='product-list-create'),
    path('api/<int:pk>', TraineeRUD.as_view(), name="apiRUD"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login (obtain token)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]


