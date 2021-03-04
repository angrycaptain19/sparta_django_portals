from django.urls import path
from infosite import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeCarouselPhotoListView.as_view(), name='home'),
    path('about', views.AboutView.as_view(), name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
