from django import contrib
from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.

def home(request):
    return render(request, "base.html")

def allCompanies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})

def getCompany(request, id):
    company = get_object_or_404(Company, id=id)
    return render(request, 'companies/companydetail.html', {'company': company})

def getProject(request, id):
    company = get_object_or_404(Company, id=id)
    projects = Project.objects.filter(company=company)
    return render(request, 'projects/project.html', {'projects': projects, 'company': company})

def getHistory(request, id):
    
    return 