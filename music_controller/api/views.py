from  .serializers import RoomSerializer
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Room

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer