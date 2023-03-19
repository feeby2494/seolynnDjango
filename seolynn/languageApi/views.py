from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import WordSerializer, LanguageSerializer, CollectionSerializer
from .models import Word, Language, Collection
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView


class LanguageListOrCreate(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'

class LanguageSingle(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'

class CollectionListOrCreate(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'

class CollectionSingle(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'

class WordListOrCreate(ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordSingle(RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer