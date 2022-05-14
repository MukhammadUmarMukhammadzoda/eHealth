from django.shortcuts import render
from rest_framework import generics

from .serializers import *

from .models import *
# Create your views here.

class IndexView(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer