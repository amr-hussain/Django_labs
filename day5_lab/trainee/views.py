from django.http import HttpResponse
from django.shortcuts import render
from .models import Trainee
from django.shortcuts import redirect 
from .forms import *
from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView #is simpler but require method overriding to handle get_context_data(), post, put methods, don't use if unless for direct redirecting using template_name 




# implementing the add using forms.form
# def trainee_add(request):
#     if request.method == "POST":
#         form = add_trainee_form(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             phone = form.cleaned_data["phone"]
#             photo = form.cleaned_data["photo"]
#             course = form.cleaned_data["course"]

    
#             trainee = Trainee(name=name, email=email, phone=phone, photo=photo, course=course)
#             trainee.save()
#             return redirect('main') 
#     else:
#         form = add_trainee_form()

#     return render(request, "trainee/add_trainee.html", {"form": form})

# class-based trainee_add 
class TraineeAdd(LoginRequiredMixin, View):
    def get(self, request):
        form = add_trainee_form()
        return render(request, "trainee/add_trainee.html", {"form": form})
    def post(self, request):
        form = add_trainee_form(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            photo = form.cleaned_data["photo"]
            course = form.cleaned_data["course"]
            trainee = Trainee(name=name, email=email, phone=phone, photo=photo, course=course)
            trainee.save()
            return redirect('main') 
        return render(request, "trainee/add_trainee.html", {"form": form})



# def trainee_delete(request, trainee_id):
#     trainee = Trainee.objects.get(id=trainee_id)
#     if request.method == "POST":
#         action = request.POST.get("action")
#         if action == "YES":
#             trainee.deleted = True
#             trainee.save()
#             return redirect('main')
#         elif action == "NO":
#             return redirect('main')

#     return render(request, "trainee/delete_trainee.html", context={"trainee": trainee})
# trainee_delete as class-based view
# adding delete auth , make sure the class LoginRequiredMixin is inherited first !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class TraineeDelete(LoginRequiredMixin, DeleteView ):
    model = Trainee
    template_name = "trainee/delete_trainee.html"
    success_url = reverse_lazy("main") 

    # in delete_trainee.html I'm using a two buttons to submit the form,
    # so I want to differntiate between them with 'action' key so I'll need to override
    # the post method of DeleteView (the parent) in order to proceed with the deletion
    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")
        if action == "YES":
            # behave normally
            return super().post(request, *args, **kwargs)
        #don't execute the post method, but redirect to main without deltetion
        return redirect(reverse_lazy("main"))




# using forms.ModelForm
# def trainee_update(request, trainee_id):
#     trainee = Trainee.objects.get(id=trainee_id)
#     if request.method == "POST":
#         form = update_trainee_form(request.POST, request.FILES, instance=trainee)
#         if form.is_valid():
#             form.save() 
#             return redirect('main')

#     else:
#         form = update_trainee_form(instance=trainee)  # instance = trainee to pre-fill fomr with existing trainee data
#     context = {"form": form, "trainee": trainee}
#     return render(request, "trainee/update_trainee.html", context)
# trainee_update as class-based view
class TraineeUpdate(LoginRequiredMixin, UpdateView):
    model = Trainee
    # form_class = update_trainee_form
    fields='__all__'
    template_name = "trainee/update_trainee.html"
    success_url = reverse_lazy("main") 




# def trainee_list(request):
#     # return HttpResponse("<h1> yes this is working </h1>")
#     trainees = Trainee.objects.filter(deleted=False)
#     return render(request, "trainee/trainee_list.html", context= {"trainees": trainees})

# list_trainee as class-based view

class TraineeList(View):
    def get(self, request):
        trainees = Trainee.objects.filter(deleted=False)
        return render(request, "trainee/trainee_list.html", context= {"trainees": trainees})
    

# login view
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
            return redirect("login")
        
        return render(request, "auth/signup.html", {"form": form})
    

####################################
# creating a api views instead of cbvs
####################################

from rest_framework import generics
from .models import Trainee
from .serializers import TraineeSerializer

class TraineeLC(generics.ListCreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

class TraineeRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

