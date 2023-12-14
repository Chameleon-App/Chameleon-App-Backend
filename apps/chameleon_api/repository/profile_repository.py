from PIL import Image

from django.conf import settings
from django.contrib.auth.models import User
from apps.chameleon_api.models import Profile


class ProfileRepository:
    @staticmethod
    def get_profile_by_user(user):
        return Profile.objects.get(user=user)

    @staticmethod
    def get_user_by_username(username: str):
        return User.objects.get(username=username)

    def post_profile_picture(self, user, photo: Image):
        profile = self.get_profile_by_user(user)
        photo.save(f"{settings.MEDIA_ROOT}/{user.username}.jpeg")
        profile.profile_photo_url = f"{user.username}.jpeg"
        profile.save()

        return profile

    def get_profile_info(self, username: str):
        user = self.get_user_by_username(username)
        return self.get_profile_by_user(user)
