from. import models
from django import forms
from django.forms import ModelForm
from .models import Trainee

# class show_trainee(ModelForm):
#     class Meta :
#         model = models.Trainee
#         fields = ['name','email','phone','photo']
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