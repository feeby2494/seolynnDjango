from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import WordSerializer
from .models import Word
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView


class WordListOrCreate(ListCreateAPIView):
     queryset = Word.objects.all()
     serializer_class = WordSerializer


# # Create your views here.
# class Word(ListCreateAPIView):
#     queryset = Word.objects.all()
#     # permission_classes = [permissions.IsAuthenticated]
#     # authentication_classes = (TokenAuthentication,) 
#     serializer_class = WordSerializer

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = WordSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):


    

class WordSingle(RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer