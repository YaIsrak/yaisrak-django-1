from django.db import models


class Pic(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=20000)
