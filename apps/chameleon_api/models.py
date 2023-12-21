import datetime
from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="profile"
    )
    profile_photo_url = models.ImageField(upload_to="", default="evlko.png")
    bio = models.TextField(max_length=500, blank=True)

    @property
    def current_streak(self) -> int:
        photo_dates = (
            RatedPhoto.objects.filter(user=self)
            .order_by("-date")
            .values_list("date", flat=True)
            .distinct()
        )
        if len(photo_dates) == 0:
            return 0
        today = datetime.datetime.today().date()
        if today != photo_dates[0]:
            return 0
        for i in range(1, len(photo_dates)):
            if (photo_dates[i - 1] - photo_dates[i]).days > 1:
                return i
        return len(photo_dates)

    @property
    def total_photos(self) -> int:
        return len(RatedPhoto.objects.filter(user=self))

    @property
    def total_rating(self) -> int:
        return RatedPhoto.objects.filter(user=self).aggregate(Sum("rating"))[
            "rating__sum"
        ]


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
