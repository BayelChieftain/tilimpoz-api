from django.db import models


class TestCategories(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='test-categories/')

    def __str__(self):
        return self.title
