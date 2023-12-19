from PIL import Image
from injector import inject

from apps.chameleon_api.repository.profile_repository import ProfileRepository
from apps.chameleon_api.service.service import ServiceInterface


class ProfileService(ServiceInterface):
    @inject
    def __init__(self, repository: ProfileRepository = None):
        if repository is None:
            repository = ProfileRepository()
        super().__init__(repository)

    def get_profile_info(self, username: str):
        return self.repository.get_profile_info(username)

    def post_profile_photo(self, user, photo_bytes):
        photo = Image.open(photo_bytes)
        return self.repository.post_profile_picture(user, photo)
