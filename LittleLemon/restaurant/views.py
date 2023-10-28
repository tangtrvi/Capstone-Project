from rest_framework.decorators import api_view
from .models import menu, booking
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet 
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import permissions

class MenuItemsView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 
