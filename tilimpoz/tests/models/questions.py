from django.db import models
from .tests import TestModel


class Question(models.Model):
    question = models.TextField()
    test = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question
