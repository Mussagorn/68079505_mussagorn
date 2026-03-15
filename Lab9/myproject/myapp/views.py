from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    allPerson = Person.objects.all()
    return render(request,"index.html",{"all Person":  allPerson})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,'form.html')

