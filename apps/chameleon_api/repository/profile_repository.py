from apps.chameleon_api.models import Profile


class ProfileRepository:
    @staticmethod
    def get_profile_by_user(user):
        return Profile.objects.filter(user=user).first()
