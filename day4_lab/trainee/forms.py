from. import models
from django import forms
from django.forms import ModelForm
from .models import Trainee
from django.contrib.auth.forms import AuthenticationForm

class update_trainee_form(forms.ModelForm):
    class Meta:
        model= Trainee
        fields='__all__'
        exclude=['deleted']

# #############################################################

class add_trainee_form(forms.Form):
    name = forms.CharField(
        required=True,min_length=3,max_length=10,label='Name'
        )
    email = forms.EmailField(label="Email", required=True)
    phone = forms.CharField(max_length=15, label="Phone", required=True)
    photo = forms.ImageField(label="Photo", required=True)
    course = forms.ModelChoiceField(queryset=models.Course.objects.all(), label="Course", required=False)


################################ login form 


class LoginFormView(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
