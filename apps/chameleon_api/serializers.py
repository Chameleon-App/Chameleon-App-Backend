from rest_framework import serializers
from .models import *


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantoneColor
        fields = ["name", "number", "hex"]


class DailyColorsSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)

    class Meta:
        model = DailyColors
        fields = "__all__"


class RatedPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatedPhoto
        fields = "__all__"
