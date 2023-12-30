from django.shortcuts import render

from django.http import HttpResponse

def home (request):
    return HttpResponse ('<H1> Electronic Reviews Home Page')

# Create your views here.
