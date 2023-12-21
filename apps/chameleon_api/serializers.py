from rest_framework import serializers
from .models import *
from .service.profile_service import ProfileService


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


class UserSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(
        source="profile.profile_photo_url", required=False
    )
    service = ProfileService()

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "profile_photo"]
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        profile_data = {}
        if "profile" in validated_data:
            profile_data = validated_data.pop("profile")

        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])

        if "profile_photo_url" in profile_data:
            profile = self.service.post_profile_photo(
                user, profile_data["profile_photo_url"].file
            )
            # TODO: profile should be assigned like this because it's called when a user is created
            user.profile = profile

        user.save()

        return user


class DaySerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    photos = serializers.SerializerMethodField("get_photos")

    class Meta:
        model = DailyColors
        fields = ["date", "colors", "photos"]

    def get_photos(self, foo):
        user = self.context["request"].user
        RatedPhotoSerializer(read_only=True, many=True)
        objects = RatedPhoto.objects.filter(date=foo.date, user=user.profile)
        serializer = RatedPhotoSerializer(
            objects,
            read_only=True,
            many=True,
            context={"request": self.context["request"]},
        )
        return serializer.data
