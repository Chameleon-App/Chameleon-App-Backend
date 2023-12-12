from celery import shared_task
from apps.chameleon_api.service.color_service import ColorService


@shared_task()
def generate_color():
    color_service = ColorService()
    color_service.generate_new_daily_color()