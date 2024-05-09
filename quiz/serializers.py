from .models import * 
from rest_framework import serializers

class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id','question','answer1','answer2','answer3','answer4')
