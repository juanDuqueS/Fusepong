from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            print("Usuario creado")
            messages.success(request, 'Usuario creado')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'social/register.html', {'form': form})