from django.shortcuts import render

from django.http import HttpResponse

def home (request):
    return HttpResponse ('<H1> Electronic Reviews Home Page')

def about (request):
    return HttpResponse ('<H1> Electronic Reviews About Us')

def contact (request):
    return HttpResponse ('<H1> Electronic Reviews Contact')

def products (request):
    return HttpResponse ('<H1> Electronic Reviews Products')

def register (request):
    return HttpResponse ('<H1> Electronic Reviews Register')

def login (request):
    return HttpResponse ('<H1> Electronics Review Login Page')

