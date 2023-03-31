import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libreriasUSB.settings')

celery_app = Celery('libreriasUSB')
celery_app.config_from_object('django.conf:settings', namespace="CELERY")
celery_app.autodiscover_task()