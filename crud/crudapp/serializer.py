from rest_framework import serializers
from .models import post

class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'
