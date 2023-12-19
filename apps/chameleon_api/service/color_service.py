from injector import inject

from apps.chameleon_api.repository.color_repository import ColorRepository
from apps.chameleon_api.utils.color_generator import ColorGenerator
from apps.chameleon_api.service.service import ServiceInterface


class ColorService(ServiceInterface):
    @inject
    def __init__(self, repository: ColorRepository):
        super().__init__(repository)

    @staticmethod
    def get_all_colors():
        return ColorRepository.get_all_colors()

    @staticmethod
    def get_last_daily_color():
        return ColorRepository.get_last_daily_color()

    @staticmethod
    def get_all_daily_colors():
        return ColorRepository.get_all_daily_colors()

    @staticmethod
    def generate_new_daily_color():
        color_generator = ColorGenerator(ColorRepository)
        colors = color_generator.generate_daily_colors()
        ColorRepository.add_daily_colors(colors)
