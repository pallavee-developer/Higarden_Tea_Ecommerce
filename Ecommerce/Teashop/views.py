from django.shortcuts import render, redirect
from . models import Product,Person

# Create your views here.
def home(request):
    item = Product.objects.all()
    return render(request,'home.html',{'item':item})

def about(request):
    return render(request,'about.html')

def contact(request):
    data = Person.objects.all()
    return render(request,'contact.html',{'data':data})

def addperson(request):
    p = Person()
    p.name = request.POST['name']
    p.email = request.POST['email']
    p.subject = request.POST['subject']
    p.message = request.POST['message']
    p.save()
    return redirect('/')


