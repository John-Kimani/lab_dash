from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePage(request):
    '''
    Function to view homepage
    '''
    return HttpResponse('<h1>Home Page Works</h1>')