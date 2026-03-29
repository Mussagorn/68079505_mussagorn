from django.shortcuts import render,redirect
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
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        person = Person.objects.create(name=name , age=age)
        return redirect("/")
    else:
        return render(request, "form.html")

# def form(request):
#     if request.method == 'POST':
#         name = request.POST.get["name"]
#         age = request.POST.get["age"]

#         Person = Person.objects.create(
#             name=name,
#             age=age
#         )
#         return  redirect("/")
#     else:
#         return render(request,"form.html")
    
    