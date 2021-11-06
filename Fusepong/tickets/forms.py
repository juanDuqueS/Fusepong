from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from .models import Ticket

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {k:"" for k in fields }

class addTicketForm(forms.ModelForm):
    name = forms.CharField(required=True)
    comments = forms.CharField(label='', widget=Textarea(attrs={'rows':2, 'placeholder':"New ticket"}))

    class Meta:
        model = Ticket
        fields = ['name', 'comments', 'finished']