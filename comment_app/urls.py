from django.urls import path
from .views import *

urlpatterns=[
    path('get/<category>',getComment),
    path('add',addComment),
    path('update/<pk>',updateComment),
    path('delete/<pk>',deleteComment),
]