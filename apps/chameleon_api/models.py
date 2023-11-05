import datetime
from django.db import models
from django.utils.translation import gettext as _


class PantoneColorPrototype(models.Model):
    hex = models.CharField(max_length=255)


class PantoneColor(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    hex = models.CharField(max_length=255)
    prototype = models.ForeignKey(
        PantoneColorPrototype, on_delete=models.SET_NULL, null=True
    )


class DailyColors(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    colors = models.ManyToManyField(PantoneColor)
