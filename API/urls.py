from django.urls import path
from .views import  *

urlpatterns = [
    path("register/",View_Register),
    path("category-product/",View_Category),
    path("type-task/",View_Task_Type),
    path("comment/",CommentView.as_view()),
]