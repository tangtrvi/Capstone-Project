from rest_framework import generics, serializers
from .models import menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['title', 'price', 'inventory']
