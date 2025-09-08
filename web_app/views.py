from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Rentals,Returns,User,Movies
from . import models
from .forms import RentalsForm,ReturnsForm
from django.http import JsonResponse
from django.utils.dateparse import parse_date
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def rentals(request):
    if request.method == "POST":
        form = RentalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rentals")
    else:
        form = RentalsForm()

    return render(request, "rentals.html", {"form": form})

def movies(request):
    movies=Movies.objects.all()
    return render(request, "movies.html", {"movies": movies})


def returns(request):
    if request.method=="POST":
        form = ReturnsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("returns")
    else:
        form = ReturnsForm()
    return render(request, "returns.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def movies_item(request,pk=None):
    if pk:
        movie=Movies.objects.get(pk=pk)
    else:
        movie=''
    return render(request, "movies_item.html",{"movie": movie})



















