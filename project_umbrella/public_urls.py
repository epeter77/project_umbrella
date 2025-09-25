# project_umbrella/public_urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView # <-- Import Django's LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # When a request comes for the root path (''), use the LoginView.
    # We must tell it which template to display.
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)