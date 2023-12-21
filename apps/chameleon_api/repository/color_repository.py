import random
import datetime

from apps.chameleon_api.models import PantoneColor, DailyColors, PantoneColorPrototype
from apps.chameleon_api.repository.repository import RepositoryInterface


class ColorRepository(RepositoryInterface):
    @staticmethod
    def get_all_colors():
        return PantoneColor.objects.all()

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
        return DailyColors.objects.latest("date")

    @staticmethod
    def get_all_daily_colors():
        return DailyColors.objects.all().order_by("-date")

    @staticmethod
    def add_daily_colors(colors):
        daily = DailyColors.objects.create()
        daily.colors.set(colors)
        daily.date = datetime.date.today()
        daily.save()
