from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from features.subscribe.app import views

urlpatterns = [
    path("", views.subscribe_view, name="subscribe"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
