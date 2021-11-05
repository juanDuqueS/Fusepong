from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.allCompanies, name='companies'),
    path('companies/<int:id>', views.getCompany, name='getCompany'),
    path('projects/<int:id>', views.getProject, name='getProject'),
    path('histories/<int:id>', views.getHistory, name='getHistory'),
    path('tickets/<int:id>', views.getTickets, name='getTicket'),
    path('addTicket/<int:id>', views.addTicket, name='addTicket'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='home.html'), name='logout'),
]
