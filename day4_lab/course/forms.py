from. import models
from django import forms
from django.forms import ModelForm
from .models import Course

class addCourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields='__all__'
        labels = {
            'name': "Course Name",
            'price': "Course Price",
        }


