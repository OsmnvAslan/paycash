import os

from celery import Celery
from celery.schedules import crontab
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


class MyCelery(Celery):
    def now(self):
        return localtime()


celery_app = MyCelery(main='core')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


celery_app.conf.beat_schedule = {
    'celery-task': {
        'task': 'transaction.tasks.update_transaction',
        'schedule': crontab(minute=0, hour=3),
    },
}
