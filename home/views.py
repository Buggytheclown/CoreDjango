from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext


def homepage (request):
    return render (request,'home/site.html' )

def contact (request):
    return render (request,'home/contact.html' )

def about (request):
    return render (request,'home/about.html' )