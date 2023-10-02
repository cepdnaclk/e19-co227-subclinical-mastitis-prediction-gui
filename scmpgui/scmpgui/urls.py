"""
URL configuration for scmpgui project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
from members.views import register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('data/', include('dataform.urls')),
    path('result/', include('results.urls')),
    path('multiple/', include('multiple.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    #! MIND THE ORDER, THIS MUST BE LAST
    path('history/',include('history.urls')),
    path('', RedirectView.as_view(url='members/',permanent=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)