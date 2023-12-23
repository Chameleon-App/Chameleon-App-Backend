from apps.chameleon_api.repository.color_repository import ColorRepository
from apps.chameleon_api.utils.color_generator import ColorGenerator
from apps.chameleon_api.service.service import ServiceInterface


class ColorService(ServiceInterface):
    repository = ColorRepository()
    generator = ColorGenerator(repository)

    def get_all_colors(self):
        return self.repository.get_all_colors()

    def get_last_daily_color(self):
        return self.repository.get_last_daily_color()

    def get_all_daily_colors(self):
        return self.repository.get_all_daily_colors()

    def generate_new_daily_color(self):
        colors = self.generator.generate_daily_colors()
        self.repository.add_daily_colors(colors)
