import io
import numpy as np
from PIL import Image

from apps.chameleon_api.utils.color_generator import Color
from apps.chameleon_api.utils.linear_interpolation import LinearInterpolation
from apps.chameleon_api.repository.photo_repository import PhotoRepository
from apps.chameleon_api.repository.color_repository import ColorRepository
from apps.chameleon_api.service.service import ServiceInterface


class PhotoRaterService(ServiceInterface):
    repository = ColorRepository()

    def __init__(self):
        self.linear_interpolation = LinearInterpolation(x1=0, x2=0.3, y1=0, y2=1)

    @staticmethod
    def harmonic_mean(arr: np.array) -> float:
        eps = 0.1
        return len(arr) / np.sum([1 / (x + eps) for x in arr])

    @staticmethod
    def mask_count(arr: np.array, color: Color, threshold: int) -> int:
        values = color.get_np_from_components()
        mask = np.full(arr.shape, True)

        for i, value in enumerate(values):
            mask[:, :, i] = mask[:, :, i] * (
                (arr[:, :, i] >= value - threshold)
                & (arr[:, :, i] <= value + threshold)
            )

        return int(np.sum(np.sum(mask, axis=2) == 3))

    def rate(self, photo: Image) -> int:
        photo_arr = np.array(photo)
        photo_size = photo_arr.shape[0] * photo_arr.shape[1]
        colors = self.repository.get_last_daily_color()
        colors = [Color(color_dict=color) for color in colors.colors.values()]
        rating = self.harmonic_mean(
            [
                self.linear_interpolation.calc(
                    self.mask_count(photo_arr, color, 10) / photo_size
                )
                for color in colors
            ]
        )

        return round(rating * 100)

    def get_rated_photo(self, photo_bytes: bytes, user):
        photo = Image.open(io.BytesIO(photo_bytes))
        rating = self.rate(photo)
        photo_repo = PhotoRepository()
        return photo_repo.add_rated_photo(photo, rating, user)
