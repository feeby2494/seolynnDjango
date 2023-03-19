"""seolynn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cgitb import handler
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView, TemplateView
import os
from django.conf import settings
from django.conf.urls.static import static

# How is this so hard! What the Fucking Hell is going on? 
favicon_view = RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('account/', include('django.contrib.auth.urls')),
    # path('api/v1/', include(('languageApi.urls', 'webServices.urls',))),
    path('api/v1/study/', include('languageApi.urls')), 
    path('api/v1/repair/', include('repairApi.urls')), 
    path('webservices/', include('webServices.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('test-mat-plt/', include('testMatPlt.urls')),
    path('favicon.ico', favicon_view, name='favicon'),
    re_path(r'^favicon\.ico$', favicon_view, name='favicon'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    re_path(r'^(?P<path>.*)/$', include('home.urls')), #Catch All path => home app
]

if os.getenv("DEBUG", "False").lower() in ("true", "1", "t"):
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'seolynn.views.handler404'