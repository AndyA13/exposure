from django.db import models


class Photo(models.Model):
    title = models.CharField(200)
    image = models.ImageField()
