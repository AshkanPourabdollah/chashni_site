from django.urls import path
from .views import *

urlpatterns=[
    path('accountList',account_list),
    path('login/<number>',account_with_number),
    path('signin',creating_account),
    path('update/<pk>',updating_account)

]