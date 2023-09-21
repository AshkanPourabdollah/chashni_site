from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializers

# Create your views here.

# getting all accounts
@api_view(["GET"])
def account_list(request):
    accounts=Account.objects.all()
    account_serialize=AccountSerializers(accounts,many=True)
    return Response(account_serialize.data)


# getting account with number(for log in)
@api_view(["GET"])
def account_with_number(request,number):
    account=Account.objects.get(phone=number)
    account_serialize=AccountSerializers(account,many=False)
    return Response(account_serialize.data)
    

# creating new account(for sign in)
@api_view(["POST"])
def creating_account(request):
    account=AccountSerializers(data=request.data)
    allAccounts=Account.objects.filter(phone=request.data['phone'])
    if account.is_valid():
        if list(allAccounts) == []:
            account.save()
            return Response(account.data)
    

# updating account
@api_view(["POST"])
def updating_account(request,pk):
    instance=Account.objects.get(id=pk)
    account=AccountSerializers(instance=instance,data=request.data)
    if account.is_valid():
        account.save()
        return Response(account.data)
    