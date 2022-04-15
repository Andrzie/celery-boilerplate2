
from django.contrib import admin
from django.urls import path
from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ctct/', ContactView.as_view(), name='contacts'),
    path('', index),
    re_path(r'^celery-progress/', include('celery_progress.urls')),

]
