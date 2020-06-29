from django.urls import path
from . import views
from pra import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.showvideo, name = 'create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)