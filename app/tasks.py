import os

from django.core.mail import send_mail
from celery import shared_task
from time import sleep
from app.models import Contact

@shared_task
def send_email_task():
        for contact in Contact.objects.all():
              send_mail('Вы у нас на странице !',
                         'Вы подписались на рассылку. Поздравляем-с !',
                         'Andrzie@fastmail.com',
                         ['mgakob@mailto.plus'],
                         fail_silently=False)
        return None


@shared_task
def send_spam(email):
    send(email)


@shared_task
def send_notifications():
    print('Here I\`m`')