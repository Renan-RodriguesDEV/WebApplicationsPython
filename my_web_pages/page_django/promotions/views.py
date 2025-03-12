from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    return render(request, "home/home.html", {"user": "Renan"})


def contact(request: HttpRequest):
    return render(request, "contact/contact.html", {"user": "Renan"})


def about(request: HttpRequest):
    context = {
        "username": "Renan",
        "email": "Renan@example.com",
        "last_name": "Rodrigues",
        "date_joined": "2021-10-10",
    }
    return render(request, "accounts/accounts.html", context)
