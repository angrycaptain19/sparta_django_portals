"""sparta_django_portals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from sparta_django_portals import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('infosite.urls')),
    path('accounts/', include('accounts.urls')),
    path('hackaton/', include('hackaton.urls')),
    path('opendata/', include('opendata.urls')),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
