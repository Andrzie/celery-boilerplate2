from django.shortcuts import render
from app.tasks import send_email_task
from django.http import HttpResponse
from .task import go_to_sleep

def index(request):
    send_email_task.delay()
    return HttpResponse('<h1> Почта отправлена by celery! </h1>')

def index(request):
    task = go_to_sleep.delay(1)
    return render(request, 'index.html', {'task_id': task.task_id})