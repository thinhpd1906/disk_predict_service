from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView

class Predict(ListCreateAPIView):
    def __init__(self) :
        self.model = {}
    def get(self, request):
        print("test cors")
        return HttpResponse("hello world")
    def post(self, request):
        return HttpResponse("post day")