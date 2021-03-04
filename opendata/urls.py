from django.urls import path
from opendata import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LocalGovernmentUnitListView.as_view(), name='opendata'),
    path('<slug:slug>/details', views.LocalGovernmentUnitDetailView.as_view(), name='localgovernmentunit_details'),
    path('list/', views.LocalGovernmentChallengeListView.as_view(), name='localgovernmentchallenge_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
