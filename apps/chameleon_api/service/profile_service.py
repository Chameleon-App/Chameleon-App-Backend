from PIL import Image

from apps.chameleon_api.repository.profile_repository import ProfileRepository
from apps.chameleon_api.service.service import ServiceInterface


class ProfileService(ServiceInterface):
    def __init__(self):
        super().__init__(ProfileRepository())

    def get_profile_info(self, username: str):
        return self.repository.get_profile_info(username)

    def post_profile_photo(self, user, photo_bytes):
        photo = Image.open(photo_bytes)
        return self.repository.post_profile_picture(user, photo)
