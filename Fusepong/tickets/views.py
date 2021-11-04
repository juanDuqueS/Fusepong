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
    project = get_object_or_404(Project, id=id)
    histories = History.objects.filter(project=project)
    return render(request,'histories/history.html', {'histories': histories, 'project': project})

def getTickets(request,id):
    history = get_object_or_404(History, id=id)
    tickets = Ticket.objects.filter(history=history)
    return render(request, 'tickets/ticket.html', {'tickets':tickets, 'history':history})