from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class History(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self) -> str:
        return self.name

class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    comments = models.TextField(blank=True)
    ##status = models.TextField()
    active = models.BooleanField(default=True)
    finished = models.BooleanField(default=False)
    createdBy = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    history = models.ForeignKey(History, related_name='history', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name