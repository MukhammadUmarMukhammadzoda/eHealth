from django.shortcuts import render

# Create your views here.
from .serializers import *
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

@api_view(['post'])
def View_Register(request):
    type_client = request.POST['type']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    if type_client == 'Expert':
        bio = request.POST['bio']
        video = request.POST['video']

    else:
        type_g = request.POST['type_g']
        type_g = request.POST['type_g']
    