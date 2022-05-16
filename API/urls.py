from django.urls import path
from .views import  *

urlpatterns = [
    path("register/",View_Register),
]