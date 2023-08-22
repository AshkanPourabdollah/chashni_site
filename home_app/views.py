from django.shortcuts import render
from .models import *
import random

# Create your views here.
'''------------------------------------------------------------------------------------------------------'''

# database
def berenj():
    list=Food.objects.all()
    return list






def cheloList():
    return Food.objects.filter(category='پلو')

def khorakList():
    return Food.objects.filter(category='خوراک')

def KhoreshList():
    return Food.objects.filter(category='خورش')


def comments():
    return Comments.objects.all()

'''------------------------------------------------------------------------------------------------------'''
def index(request):
    return render(request,"home_app/index.html",context={"chelo":cheloList(),"khorak":khorakList(),"khoresh":KhoreshList()})

def about(request):
    return render(request,"home_app/about.html")

def contact(request):
    return render(request,"home_app/contact.html")

def menu(request):
    return render(request,"home_app/menu.html",context={"chelo":cheloList(),"khorak":khorakList(),"khoresh":KhoreshList()})

def findFood(food):
    for chelo in  cheloList():
        if chelo.foodName == food:
            return chelo
    for khorak in khorakList():
        if khorak.foodName == food:
            return khorak
    for khoresh in KhoreshList():
        if khoresh.foodName == food:
            return khoresh
        
def foodDetails(request,food):
    return render(request,"home_app/food.html",context={"foodDetail":findFood(food)})

def showComment(request):
    randomComments=random.sample(list(comments()),5)
    return render(request,"home_app/comments.html",context={"comments":randomComments})