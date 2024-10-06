from django.shortcuts import render
from django.http import HttpResponse

def tester_home(request):
    return HttpResponse("This is the home page of the app tester")

def p2(request):
    return HttpResponse("This is the second page of the app tester")