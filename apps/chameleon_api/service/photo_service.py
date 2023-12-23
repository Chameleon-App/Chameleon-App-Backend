from datetime import datetime
from apps.chameleon_api.repository.photo_repository import PhotoRepository
from apps.chameleon_api.service.service import ServiceInterface


class PhotoService(ServiceInterface):
    repository = PhotoRepository()

    def get_most_rated_photos(self, date: datetime.date, offset: int, limit: int):
        return self.repository.get_most_rated_photos(date, offset, limit)
