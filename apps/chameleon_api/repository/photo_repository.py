import datetime
from PIL import Image

from django.conf import settings
from apps.chameleon_api.models import RatedPhoto
from apps.chameleon_api.repository.profile_repository import ProfileRepository
from apps.chameleon_api.repository.repository import RepositoryInterface


class PhotoRepository(RepositoryInterface):
    @staticmethod
    def get_new_path(photo: Image) -> str:
        return str(hash(photo.tobytes()))

    @staticmethod
    def get_most_rated_photos(date: datetime.date, offset: int, limit: int):
        objects = RatedPhoto.objects.all().order_by("rating")
        if date:
            objects = objects.filter(date=date)
        return objects[offset : offset + limit]

    def add_rated_photo(self, photo: Image, rating: int, user):
        path = self.get_new_path(photo)
        photo.save(f"{settings.MEDIA_ROOT}/{path}.jpeg")
        rated_photo = RatedPhoto()
        rated_photo.date = datetime.date.today()
        rated_photo.rating = rating
        rated_photo.image_url = f"{path}.jpeg"

        profile_repo = ProfileRepository()
        rated_photo.user = profile_repo.get_profile_by_user(user)

        rated_photo.save()
        return rated_photo
