from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    allPerson = Person.objects.all()
    context = {
        'allPerson': allPerson
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,'form.html')

