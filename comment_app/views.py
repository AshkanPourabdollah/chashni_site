from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home_app.models import Comments
from .serializers import CommentSerialize



# Create your views here.

# getting food comments
@api_view(["GET"])
def getComment(request,category):
    comments=Comments.objects.filter(category=category)
    comment_serialize=CommentSerialize(comments,many=True)
    return Response(comment_serialize.data)

# adding food comment from android
@api_view(["POST"])
def addComment(request):
    comment=CommentSerialize(data=request.data)
    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    
# updating food comment(to make showing parameter true or false)
# updating account
@api_view(["POST"])
def updateComment(request,pk):
    instance=Comments.objects.get(id=pk)
    comment=CommentSerialize(instance=instance,data=request.data)
    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    
# deleting food comment
@api_view(["DELETE"])
def deleteComment(request,pk):
    instance=Comments.objects.get(id=pk)
    instance.delete()
    return Response("success")
