from django.http import HttpRequest
from django.shortcuts import render
from .models import Usuarios


# Create your views here.
def index(request: HttpRequest):
    return render(request, "home/home.html", {"user": "Renan"})


def contact(request: HttpRequest):
    return render(request, "contact/contact.html", {"user": "Renan"})


def about(request: HttpRequest):
    user = Usuarios.objects.first()
    return render(request, "accounts/accounts.html", {"user": user})
