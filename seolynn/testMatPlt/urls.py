from django.urls import path
from .views import TestMatPlt1

urlpatterns = [
    path('test/', TestMatPlt1.as_view(), name='testMatPlt1'),
    # re_path(r'^(?P<path>.*)/$', include('home.urls')), #Catch All path => home app
]