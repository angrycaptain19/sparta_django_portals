from django.urls import path
from accounts import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.RegisterCreateView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
