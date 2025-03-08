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
    course_id = request.POST.get('course_id')
    course_name = request.POST.get('course_name')
    global course_data
    course_data.append([course_id, course_name])
    return HttpResponse("Course stored successfully!")

def update_course(request, course_id):
    return HttpResponse(f"<h1>updating course with id {course_id}</h1>")

def delete_course(request, course_id):
    return HttpResponse(f"<h1>deleted coures with id {course_id}</h1>")

