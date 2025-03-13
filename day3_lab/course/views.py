from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import addCourseForm
from .models import Course

# Create your views here.



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/show_courses.html', context={'courses': courses})


def add_course(request):
    if request.method == 'POST':
        form = addCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else : 
            print(form.errors.as_data)
    else:
        form = addCourseForm()
    return render(request, 'course/add_course.html', {'form': form})

def update_course(request, course_id):
    return HttpResponse(f"<h1>updating course with id {course_id}</h1>")

def delete_course(request, course_id):
    return HttpResponse(f"<h1>deleted coures with id {course_id}</h1>")

