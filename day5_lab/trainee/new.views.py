# Standard library imports
import requests

# Django imports
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Local imports
from .models import Trainee
from .forms import add_trainee_form, LoginFormView
from .serializers import TraineeSerializer

# DRF imports
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# API Views
class TraineeLC(generics.ListCreateAPIView):
    queryset = Trainee.objects.filter(deleted=False)
    serializer_class = TraineeSerializer

class TraineeRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

# CBVs
class TraineeList(View):
    def get(self, request):
        response = requests.get(f'{settings.API_BASE_URL}/api/trainees/')
        trainees = response.json()
        return render(request, "trainee/trainee_list.html", context={"trainees": trainees})

class TraineeAdd(LoginRequiredMixin, View):
    def get(self, request):
        form = add_trainee_form()
        return render(request, "trainee/add_trainee.html", {"form": form})

    def post(self, request):
        form = add_trainee_form(request.POST, request.FILES)
        if form.is_valid():
            response = requests.post(f'{settings.API_BASE_URL}/api/trainees/', data=form.cleaned_data)
            if response.status_code == 201:
                return redirect('main')
        return render(request, "trainee/add_trainee.html", {"form": form})

class TraineeUpdate(LoginRequiredMixin, UpdateView):
    model = Trainee
    fields = '__all__'
    template_name = "trainee/update_trainee.html"
    success_url = reverse_lazy("main")

class TraineeDelete(LoginRequiredMixin, DeleteView):
    model = Trainee
    template_name = "trainee/delete_trainee.html"
    success_url = reverse_lazy("main")

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        if action == "YES":
            return super().post(request, *args, **kwargs)
        return redirect(reverse_lazy("main"))

class Login(LoginView):
    LoginForm = LoginFormView
    template_name = "auth/login.html"

class Logout(View):
    def post(self, request):
        logout(request)
        return redirect("main")

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "auth/signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect("main")
        return render(request, "auth/signup.html", {"form": form})