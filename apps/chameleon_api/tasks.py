from celery import shared_task
from apps.chameleon_api.service.color_service import ColorService
from apps.chameleon_api.repository.color_repository import ColorRepository


@shared_task()
def generate_color():
    color_repository = ColorRepository()
    color_service = ColorService(repository=color_repository)
    color_service.generate_new_daily_color()
