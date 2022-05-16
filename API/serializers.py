from .models import *
from rest_framework.serializers import ModelSerializer

class LoaderCategoryProduct(ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = "__all__"

class LoaderProduct(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class LoaderSport(ModelSerializer):
    class Meta:
        model = Sport
        fields = "__all__"

class LoaderDay(ModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"

class LoaderExpert(ModelSerializer):
    class Meta:
        model = Expert
        fields = "__all__"

class LoaderUser(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LoaderHistoryReyting(ModelSerializer):
    class Meta:
        model = HistoryReyting
        fields = "__all__"

class LoaderTaskSport(ModelSerializer):
    class Meta:
        model = TaskSport
        fields = "__all__"

class LoaderTaskDieta(ModelSerializer):
    class Meta:
        model = TaskDieta
        fields = "__all__"

class LoaderAdvice(ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"
