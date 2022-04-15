from django.core.mail import send_mail
from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder


@shared_task
def send_email_task():
    sleep(1)
    send_mail('Вы у нас на странице !',
              'Вы подписались на рассылку. Поздравляем-с !',
              'Andrzie@fastmail.com',
              ['mgakob@mailto.plus'],
              fail_silently=False)
    return None

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(100):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 100, f'On inter {i}')
    return 'Done'