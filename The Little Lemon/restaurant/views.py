{\rtf1\ansi\ansicpg1252\cocoartf2753
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from django.shortcuts import render\
from rest_framework import generics, viewsets\
from rest_framework.permissions import IsAuthenticated\
from .models import MenuItem, Booking\
from .serializers import MenuItemSerializer, BookingSerializer\
from rest_framework.response import Response\
\
# Create your views here.\
def index(request):\
    return render(request, 'index.html', \{\})\
\
class MenuItemsView(generics.ListCreateAPIView):\
    permission_classes=[IsAuthenticated]\
    queryset = MenuItem.objects.all()\
    serializer_class = MenuItemSerializer\
\
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):\
    permission_classes=[IsAuthenticated]\
    queryset = MenuItem.objects.all()\
    serializer_class = MenuItemSerializer\
\
class BookingViewSet(viewsets.ModelViewSet):\
    permission_classes=[IsAuthenticated]\
    queryset = Booking.objects.all()\
    serializer_class = BookingSerializer}