from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'finished', 'createdBy', 'created', 'updated']
    list_filter = ['active', 'finished']