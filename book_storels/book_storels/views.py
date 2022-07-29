import http
from django.shortcuts import render
from django.shortcuts import HttpResponse

def power(request):
    number = int(request.GET['number']) 
    number = number*number
    return HttpResponse(f'<h1>{number}</h1>')

def hello(request):
    return HttpResponse('<h1>Helloooo</h1>')