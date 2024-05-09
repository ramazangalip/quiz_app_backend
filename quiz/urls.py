from django.urls import path
from .views import *

urlpatterns = [
    path('answers/',AllQuiz.as_view())
]