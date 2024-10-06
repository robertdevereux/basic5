from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.db.utils import OperationalError

def tester_home(request):
    return HttpResponse("This is the home page of the app tester")

def p2(request):
    return HttpResponse("This is the second page of the app tester")

# tester/views.py
def check_db_connection(request):
    db_conn = connections['default']
    try:
        db_conn.cursor()
        return HttpResponse("Database connection successful!")
    except OperationalError:
        return HttpResponse("Database connection failed!")
