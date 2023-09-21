from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',index),
    path('about/',about),
    path('contact/',contact),
    path('menu/',menu),
    path('menu/<food>/',foodDetails),
    path('comments/',showComment),
    path('updateFood/<pk>',updateFood),
    path('foodList',food_List),
    path('delete/<pk>',deleteFood)
    
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)