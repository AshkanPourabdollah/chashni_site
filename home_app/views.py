from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer
from .models import *
import random

# Create your views here.
'''------------------------------------------------------------------------------------------------------'''

# database


def cheloList():
    return Food.objects.filter(category='چلو')

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
    name=request.GET.get("name_about")
    phone=request.GET.get("phone_about")
    subject=request.GET.get("subject_about")
    message=request.GET.get("message_about")
    if name!=None and phone!=None and subject!=None and message!=None:
        if name!="" and phone!="" and subject!="" and message!="":
            CommentAbout.objects.create(name=name,phone=phone,subject=subject,text=message)
            return redirect('/contact/')

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
    name=request.GET.get("name_comment")
    commentText=request.GET.get("message_comment")
    type=findFood(food)

    if name !=None and commentText != None:
        if name!= '' and commentText != '':
            Comments.objects.create(personName=name,commentText=commentText,showing=False,category=type)
            return redirect('/menu/'+type.foodName+'/')
    return render(request,"home_app/food.html",context={"foodDetail":type})

def showComment(request):
    randomComments=random.sample(list(comments()),5)
    return render(request,"home_app/comments.html",context={"comments":randomComments})

"""-------------------------------------------------------------------------------------------------------------------------------------"""
@api_view(["GET"])
def food_List(request):
    food=Food.objects.all()
    food_serializer=FoodSerializer(food,many=True)
    return Response(food_serializer.data)

# update food
@api_view(["POST"])
def updateFood(request,pk):
    food=FoodSerializer(data=request.data)
    if food.is_valid():
        pass
    print(food.data)
    instance=Food.objects.get(id=pk)
    instance.foodName=food.data['foodName']
    instance.foodPrice=food.data['foodPrice']
    instance.category=food.data['category']
    instance.isExist=food.data['isExist']
    instance.save()
    
    return Response("done")

# delete food
@api_view(["DELETE"])
def deleteFood(request,pk):
    instance=Food.objects.get(id=pk)
    instance.delete()
    return Response("success")