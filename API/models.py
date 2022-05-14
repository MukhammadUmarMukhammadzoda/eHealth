from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TaskSport(models.Model):
    pass

class TaskDieta(models.Model):
    pass

class TaskAll(models.Model):
    pass

class Product(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=255)
    video = models.URLField()
    def __str__(self):
        return self.name

class Client(AbstractUser):
    type_g = [
        (1, "Erkak"),
        (2,"Ayol")]
    gender = models.CharField(max_length=30, choices=type_g)
    register_date = models.DateField(auto_now=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    task_sport = models.ManyToManyField(TaskSport,)
    task_sport_can_not = models.ManyToManyField(Sport,)

    task_dieta = models.ManyToManyField(TaskDieta)
    task_dieta_can_not = models.ManyToManyField(Sport, related_name="NoDieta")
    
    task_all = models.ManyToManyField(TaskAll,)
    
    def __str__(self): 
        return self.username