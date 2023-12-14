from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


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
    image_url = serializers.ImageField(
        max_length=None,
        use_url=True,
    )

    class Meta:
        model = RatedPhoto
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    photos = RatedPhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = "__all__"
