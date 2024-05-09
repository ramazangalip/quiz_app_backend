from django.db import models

class Quiz(models.Model):
    question = models.CharField(max_length=200)
    answer1 = models.CharField(max_length=50)
    answer2 = models.CharField(max_length=50)
    answer3 = models.CharField(max_length=50)
    answer4 = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.question
