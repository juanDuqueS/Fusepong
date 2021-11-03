from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.allCompanies, name='companies'),
    path('companies/<int:id>', views.getCompany, name='getCompany'),
    path('projects/<int:id>', views.getProject, name='getProject'),
    path('histories/<int:id>', views.getHistory, name='getHistory')
]
