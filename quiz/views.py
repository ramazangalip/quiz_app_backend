from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import  ListAPIView
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


class AllQuiz(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers
