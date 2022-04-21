
import os
from celery import Celery
from celery.schedules import crontab
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-5-minute': {
        'task': 'app.tasks.send_email_task',
        'schedule': crontab(minute='*/5')
    }
}



