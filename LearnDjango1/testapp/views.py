from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def about(request):
    return HttpResponse('<h1>About Page</h1>')