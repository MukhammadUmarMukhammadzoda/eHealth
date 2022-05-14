from multiprocessing.connection import Client
from django.contrib import admin
from .models import *

from API.models import Product, Sport, TaskAll, TaskDieta, TaskSport

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sport)
admin.site.register(TaskSport)
admin.site.register(TaskDieta)
admin.site.register(TaskAll)
