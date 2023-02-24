from django.urls import include, path
# from rest_framework import routers
from .views import WordListOrCreate, WordSingle


app_name = 'languageApi'

# router = routers.DefaultRouter()
# router.register(r'word', Word, 'word')


urlpatterns = [
    path('word/', WordListOrCreate.as_view(), name='wordListOrCreate'),
    path('word/<int:pk>', WordSingle.as_view(), name='wordSingle'),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]