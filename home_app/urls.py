from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('about/',about),
    path('contact/',contact),
    path('menu/',menu),
    path('menu/<food>/',foodDetails),
    path('comments/',showComment),

    path('foodList',food_List)
    
]