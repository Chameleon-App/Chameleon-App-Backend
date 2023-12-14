from datetime import datetime
from apps.chameleon_api.repository.photo_repository import PhotoRepository


class PhotoService:
    @staticmethod
    def get_most_rated_photos(date: datetime.date, offset: int, limit: int):
        return PhotoRepository.get_most_rated_photos(date, offset, limit)
