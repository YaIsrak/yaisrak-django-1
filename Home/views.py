from django.shortcuts import render
from django.http import HttpResponse
from .models import Pic


def home(request):
    global pics
    pics = Pic.objects.all()
    return render(request, "Home\home.html", {'pics': pics})


def pictures(request):
    return render(request, 'Home\pic.html')