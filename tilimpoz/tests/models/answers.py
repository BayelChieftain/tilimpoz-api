from django.db import models
from .questions import Question


class Answer(models.Model):
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.answer
