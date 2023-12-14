from apps.chameleon_api.models import Profile
from django.contrib.auth.models import User


class ProfileRepository:
    @staticmethod
    def get_profile_by_user(user):
        return Profile.objects.get(user=user)

    @staticmethod
    def get_user_by_username(username: str):
        return User.objects.get(username=username)

    def get_profile_info(self, username: str):
        user = self.get_user_by_username(username)
        return self.get_profile_by_user(user)
