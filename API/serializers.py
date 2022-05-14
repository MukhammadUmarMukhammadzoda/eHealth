from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
    

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class HistoryReytingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryReyting
        fields = "__all__"

class TaskSportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSport
        fields = "__all__"

class TaskDietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDieta
        fields = "__all__"

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = "__all__"


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"

