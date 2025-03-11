from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/show_courses.html', context={'courses': courses})


def add_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')
        return HttpResponse("Course stored successfully!")
    else:
        return render(request, 'course/add_course.html')

def update_course(request, course_id):
    return HttpResponse(f"<h1>updating course with id {course_id}</h1>")

def delete_course(request, course_id):
    return HttpResponse(f"<h1>deleted coures with id {course_id}</h1>")

