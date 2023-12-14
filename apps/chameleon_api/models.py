import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="profile")
    profile_photo_url = models.ImageField(upload_to="", default="evlko.png")
    bio = models.TextField(max_length=500, blank=True)
    current_streak = models.IntegerField(default=0)
    total_photos = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)


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


class RatedPhoto(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name="photos"
    )
    image_url = models.ImageField(upload_to="")
    date = models.DateField(_("Date"), default=datetime.date.today)
    rating = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
