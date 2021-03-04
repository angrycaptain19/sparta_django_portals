from django.urls import path
from hackaton import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HackatonChallengeListView.as_view(), name='hackatonchallenge_list'),
    path('<slug:slug>/details', views.HackatonChallengeDetailView.as_view(), name='hackatonchallenge_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
