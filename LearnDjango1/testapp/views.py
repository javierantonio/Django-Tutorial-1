from django.shortcuts import render
from django.http import HttpResponse

def home(request):
<<<<<<< HEAD
    return HttpResponse('<h1>Hello This is test file+</h1>')
=======
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def about(request):
    return HttpResponse('<h1>About Page</h1>')
>>>>>>> Episode-3
