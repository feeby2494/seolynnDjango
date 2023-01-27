from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse('This is HomeView Class View.')

def home(request):
    print(request.user)
    return HttpResponse('This is Home View.')

