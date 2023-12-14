from apps.chameleon_api.repository.profile_repository import ProfileRepository


class ProfileService:
    @staticmethod
    def get_profile_info(username: str):
        profile_repo = ProfileRepository()
        return profile_repo.get_profile_info(username)
