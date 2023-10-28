from django.db import models


class PantoneColor(models.Model):
    name = models.CharField(max_length=255)
