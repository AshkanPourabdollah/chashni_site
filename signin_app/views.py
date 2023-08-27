from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def signinMain(request):
    return render(request,"signin_app/booking.html")
def register(request):
    if request.method == 'POST':
        person=SigninForm(request.POST)
        if person.is_valid():
            data=person.cleaned_data
            if data['password']==data['confirmPassword']:
                Signin.objects.create(
                    name=data['name'],
                    phone=data['phone'],
                    password=data['password'],
                    confirmPassword=data['confirmPassword'])
        
        return redirect('index')
            
    else:
        person=SigninForm()
    return render(request,"signin_app/register.html",context={"form":person})

def book(request):
    person=SigninForm()
    return render(request,"signin_app/booking.html",context={"form":person})