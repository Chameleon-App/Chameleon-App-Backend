import datetime
from PIL import Image

from django.conf import settings
from apps.chameleon_api.models import RatedPhoto


class PhotoRepository:
    @staticmethod
    def get_new_path(photo: Image) -> str:
        return str(hash(photo.tobytes()))

    @staticmethod
    def get_most_rated_photos(filter_date: datetime.date):
        if filter_date is None:
            return RatedPhoto.objects.all().order_by("rating")
        return RatedPhoto.objects.filter(date=filter_date).order_by("rating")

    def add_rated_photo(self, photo: Image, rating: int):
        path = self.get_new_path(photo)
        photo.save(f'{settings.MEDIA_ROOT}{path}.jpeg')
        rated_photo = RatedPhoto()
        rated_photo.date = datetime.date.today()
        rated_photo.rating = rating
        rated_photo.image_url = path
        rated_photo.save()
        return rated_photo
