from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']



# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'order']