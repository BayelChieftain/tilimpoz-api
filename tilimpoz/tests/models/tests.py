from django.db import models


class TestModel(models.Model):
    title = models.CharField(max_length=350)

    def __str__(self):
        return self.title
