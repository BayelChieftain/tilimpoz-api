from django.db import models
from .questions import Question


class Answer(models.Model):
    answer = models.TextField()
    nickname = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer
