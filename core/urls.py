
from django.contrib import admin
from django.urls import path
from app.views import index, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ctct/', ContactView.as_view(), name='contacts'),
    path('', index),
]
