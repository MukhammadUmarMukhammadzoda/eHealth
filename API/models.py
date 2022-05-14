from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TaskSport(models.Model):
    pass

class TaskDieta(models.Model):
    pass

class TaskAll(models.Model):
    pass

class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=255)
    video = models.URLField()
    def __str__(self):
        return self.name

class Client(AbstractUser):
    type_g = (
        (1, "Erkak"),
        (2,"Ayol"))
    gender = models.IntegerChoices(type_g)
    register_date = models.DateField(auto_now=True)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.FloatField()
    task_sport = models.ManyToManyField(TaskSport,null=True,blank=True)
    task_sport_can_not = models.ManyToManyField(Sport,null=True,blank=True)

    task_dieta = models.ManyToManyField(TaskDieta,null=True,blank=True)
    task_dieta_can_not = models.ManyToManyField(Sport,null=True,blank=True)
    
    task_all = models.ManyToManyField(TaskAll,null=True,blank=True)
    
    def __str__(self): 
        return self.username