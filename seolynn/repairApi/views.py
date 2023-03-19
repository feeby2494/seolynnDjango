from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View

# Create your views here.
class RepairHome(View):
    def get(self, request):
        return JsonResponse({'message' : "User's home"})
    
class RepairOrderList(View):
    def get(self, request):
        return JsonResponse({'message' : "All orders for this one user"})
    
class RepairOrder(View):
    def get(self, request):
        return JsonResponse({'message' : "All Repairs for this one order"})
    
class Repair(View):
    def get(self, request):
        return JsonResponse({'message' : "All details for one single Repair"})