from django.urls import path
from .views import *

urlpatterns = [
    path('all',allOrders),
    path('person/<number>',personOrders),
    path('save',saveOrders)
]