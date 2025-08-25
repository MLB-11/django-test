from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Vue pour la page d'accueil HTML
def index(request):
    return render(request, 'index.html', {})

# API Views
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [AllowAny] # Tout le monde peut voir le menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] # Seuls les utilisateurs connectés peuvent gérer les réservations
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer