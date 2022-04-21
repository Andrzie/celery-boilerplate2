from django.views.generic import CreateView
from django.shortcuts import render
from app.tasks import send_email_task
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

def index(request):
    #send_email_task.delay()
    return HttpResponse('<h1> Почта отправлена by celery! </h1>')

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contacts.html'

    def form_valid(self, form):
        form.save()
        send_spam.delay(form.instance.email)
        return super().form_valid(form)

