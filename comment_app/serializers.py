from rest_framework import serializers
from home_app.models import Comments

class CommentSerialize(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields="__all__"