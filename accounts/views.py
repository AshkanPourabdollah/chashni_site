from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .form import *



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            User.objects.create_user(data['username'],data['email'],data['password'])
            return redirect('index')
    else:
        form=UserRegistrationForm()
    return render(request,"accounts/register.html",{'form':form})