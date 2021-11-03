from django import contrib
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "base.html")

def allCompanies(request):
    companies = Company.objects.all()
    return render(request, 'tickets/company.html', {'companies': companies})