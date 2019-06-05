from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for error tree users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    """
    Endpoint for board administrator
    """
    queryset = Admin.objects.all() #decide what to order on later
    serializer_class = AdminSerializer

class GateViewSet(viewsets.ModelViewSet):
    """
    Endpoint for gate
    """
    queryset = Gate.objects.all()
    serializer_class = GateSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    Event/note API - the heart of the content
    """
    # Wish there were a slightly more semantic/less loaded word...event can be so many things in programming...
    queryset = Event.objects.all()
    serializer_class = EventSerializer
