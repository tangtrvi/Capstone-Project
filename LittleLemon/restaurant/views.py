from rest_framework.decorators import api_view
from .models import menu
from rest_framework import generics
from .serializers import MenuSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer