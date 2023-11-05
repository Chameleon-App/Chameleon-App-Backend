import random
import datetime

from apps.chameleon_api.models import PantoneColor, DailyColors, PantoneColorPrototype


class ColorRepository:
    @staticmethod
    def get_color_by_id(color_id):
        return PantoneColor.objects.get(id=color_id)

    @staticmethod
    def get_random_color():
        random_id = random.randint(0, PantoneColor.objects.count())
        return PantoneColor.objects.get(id=random_id)

    @staticmethod
    def get_prototype_colors(prototypes_id):
        return PantoneColor.objects.filter(prototype__in=prototypes_id)

    @staticmethod
    def get_all_prototypes():
        return PantoneColorPrototype.objects.all()

    @staticmethod
    def get_last_daily_color():
        return DailyColors.objects.latest("id")

    @staticmethod
    def add_daily_colors(colors_id):
        daily = DailyColors()
        daily.save()
        for color_id in colors_id:
            color = PantoneColor.objects.get(id=color_id)
            daily.colors.add(color)
        daily.date = datetime.date.today()
