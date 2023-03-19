from django.urls import include, path
# from rest_framework import routers
from .views import WordListOrCreate, WordSingle, LanguageSingle, LanguageListOrCreate


app_name = 'languageApi'

# router = routers.DefaultRouter()
# router.register(r'word', Word, 'word')


urlpatterns = [
    path('language/', LanguageListOrCreate.as_view(), name='LanguageListOrCreate'),
    path('language/<slug:language_slug>/', LanguageSingle.as_view(), name='LanguageSingle'),
    path('language/<slug:language_slug>/words/', WordListOrCreate.as_view(), name='wordListOrCreate'),
    path('language/<slug:language_slug>/words/<int:word_id>/', WordSingle.as_view(), name='wordSingle'),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]