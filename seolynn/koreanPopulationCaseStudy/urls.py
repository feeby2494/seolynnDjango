from django.urls import path
from .views import KoreanPopulation

urlpatterns = [
    path('korean-population/', KoreanPopulation.as_view(), name='koreanPopulation'),
    # re_path(r'^(?P<path>.*)/$', include('home.urls')), #Catch All path => home app
]