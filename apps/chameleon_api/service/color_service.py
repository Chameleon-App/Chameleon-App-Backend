from apps.chameleon_api.repository.color_repository import ColorRepository


class ColorService:
    @staticmethod
    def get_all_colors():
        return ColorRepository.get_all_colors()

    @staticmethod
    def get_last_daily_color():
        return ColorRepository.get_last_daily_color()
