from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'generate-color': {
        'task': 'apps.chameleon_api.tasks.generate_color',
        'schedule': timedelta(minutes=1),
    },
}

app.conf.timezone = 'UTC'