import io

from PIL import Image

from apps.chameleon_api.repository.profile_repository import ProfileRepository


class ProfileService:
    @staticmethod
    def get_profile_info(username: str):
        profile_repo = ProfileRepository()
        return profile_repo.get_profile_info(username)

    @staticmethod
    def post_profile_photo(user, photo_bytes):
        photo = Image.open(photo_bytes)
        profile_repo = ProfileRepository()
        return profile_repo.post_profile_picture(user, photo)
