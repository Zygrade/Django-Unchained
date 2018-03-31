from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse('This is the about page, under construction')
    return render(request,'about.html')

def homepage(request):
    #return HttpResponse('This is the homepage, under construction')
    return render(request,'homepage.html')
