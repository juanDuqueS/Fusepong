from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def allCompanies(request):
    if not request.user.is_authenticated:
        return redirect('login')
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})

def getCompany(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    company = get_object_or_404(Company, id=id)
    return render(request, 'companies/companydetail.html', {'company': company})

def getProject(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    company = get_object_or_404(Company, id=id)
    projects = Project.objects.filter(company=company)
    return render(request, 'projects/project.html', {'projects': projects, 'company': company})

def getHistory(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    project = get_object_or_404(Project, id=id)
    histories = History.objects.filter(project=project)
    return render(request,'histories/history.html', {'histories': histories, 'project': project})

def getTickets(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    history = get_object_or_404(History, id=id)
    tickets = Ticket.objects.filter(history=history)
    return render(request, 'tickets/ticket.html', {'tickets':tickets, 'history':history})

def addTicket(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = get_object_or_404(User, pk=request.user.pk)
    history = get_object_or_404(History, id=id)
    if request.method == 'POST':
        form = addTicketForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.history = history
            post.save()
            return redirect('getTicket', id=history.id)
    else:
        form = addTicketForm()
    return render(request, 'tickets/addTicket.html', {'form': form})

def statusTicket(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    ticket = get_object_or_404(Ticket, id=id)
    if ticket.finished:
        Ticket.objects.filter(id=id).update(finished=False)
    else:
        Ticket.objects.filter(id=id).update(finished=True)

    return redirect('getTicket', id=ticket.history.id)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'social/register.html', {'form': form})