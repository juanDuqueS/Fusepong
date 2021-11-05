from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    nit = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(default="No description")
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class History(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(default="No description")
    finished = models.BooleanField(default=False)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self) -> str:
        return self.name

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    comments = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    finished = models.BooleanField(default=False)
    history = models.ForeignKey(History, related_name='history', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name