from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


course_data =  [
    [1, 'Python'],
    [2, 'PHP'],
    [3, 'Java'],
    [2, 'HTML'],
    [3, 'Pascal'],
]

def course_list(request):

    return render(request, 'course/show_courses.html', context={'list': course_data})

def add_course(request):
    pass

def update_course(request, course_id):
    return HttpResponse(f"<h1>updating course with id {course_id}</h1>")

def delete_course(request, course_id):
    return HttpResponse(f"<h1>deleted coures with id {course_id}</h1>")

