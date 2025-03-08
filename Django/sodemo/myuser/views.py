from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Define view
# HttpResponse---doment.write
def Loginview(req):
    return  HttpResponse('<h1>login from view</h1>')
def logoutview(request):
    print(request,type(request))
    print(request.method)
    print(request.GET)
    obj=HttpResponse('<h1>hi</h1>')
    obj.write('<h2>hi</h2>')
    obj['content-type']='text/plain'
    return obj

def Regview(req):
    obj=HttpResponse()
    obj.write('''
    <form>
    
    </form>''')
    return obj