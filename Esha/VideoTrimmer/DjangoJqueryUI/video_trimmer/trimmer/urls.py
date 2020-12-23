
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('trim', views.trim, name='trim'),
    path('result', views.result, name='trim'),
    path('result2', views.result2, name='trim'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
