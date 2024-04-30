from django.urls import path, include
from .views import Predict

urlpatterns = [
    path("hello/", Predict().as_view()),
]