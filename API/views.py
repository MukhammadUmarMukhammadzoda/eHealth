from django.shortcuts import render
import datetime
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

def check_algoritm(obj):
    pass

@api_view(['post'])
def View_Register(request):
    type_client = request.POST['type']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    if len(User.objects.filter(username=username)) == 0:
        if type_client == '2':
            bio = request.POST['bio']
            video = request.POST['video']
            user = User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=int(type_client),bio=bio,video=video)
        else:
            type_g = request.POST['type_g']
            register_date = datetime.datetime.now()
            age = request.POST['age']
            height = request.POST['height']
            weight = request.POST['weight']
            type_t = request.POST['type_t']
            can_not_dieta = []
            can_not_sports = []
            if type_t == 1 or type_t == 3:
                not_sports = request.POST['can_not_sports']
                for id in not_sports:
                    can_not_sports.append(Sport.objects.get(id=id))
                
            if type_t == 2 or type_t == 3:
                not_dieta = request.POST['can_not_dieta']
                for id in not_dieta:
                    can_not_dieta.append(Product.objects.get(id=id))
            user = User.objects.create(
                gender=type_g,register_date=register_date,week_result=weight,age=age,
                weight=weight,height=height,task_sport_can_not=can_not_sports,task_dieta_can_not=can_not_dieta,task_type=type_t,
                username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=type_client)
        token_key = Token.objects.create(user=user)
        DATA = {
                "username":username,
                "key":str(token_key),
                "type_client":type_client,
            }
        return Response(DATA)
    else:
        return Response(status=400)
