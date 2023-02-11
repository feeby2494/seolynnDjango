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
from django.views.generic.base import RedirectView

# How is this so hard! What the Fucking Hell is going on? 
favicon_view = RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('webservices/', include('webServices.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('test-mat-plt/', include('testMatPlt.urls')),
    # I mean what the Hell is going on with the favicon? How can I get a 500 or 404 with this?
    path('static/favicon.ico', favicon_view, name='favicon'),
    path('favicon.ico', favicon_view, name='favicon'),
    re_path(r'^favicon\.ico$', favicon_view, name='favicon'),
    # re_path(r'^(?P<path>.*)/$', include('home.urls')), #Catch All path => home app
]

handler404 = 'seolynn.views.handler404'