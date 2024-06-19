from django.db import models


# Create your models here.

class Question(models.Model):
    question = models.TextField()
    nickname = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

