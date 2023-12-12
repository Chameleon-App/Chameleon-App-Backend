from apps.chameleon_api.repository.color_repository import ColorRepository
from apps.chameleon_api.utils.color_generator import ColorGenerator


class ColorService:
    @staticmethod
    def get_all_colors():
        return ColorRepository.get_all_colors()

    @staticmethod
    def get_last_daily_color():
        return ColorRepository.get_last_daily_color()

    @staticmethod
    def generate_new_daily_color():
        color_generator = ColorGenerator(ColorRepository)
        colors = color_generator.generate_daily_colors()
        ColorRepository.add_daily_colors(colors)
