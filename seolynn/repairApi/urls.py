from django.urls import include, path
from django.http.response import HttpResponse
from .views import RepairHome, RepairOrderList, RepairOrder, Repair



urlpatterns = [
    path('', RepairHome.as_view(), name='repairHome'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('orders/', RepairOrderList.as_view(), name='repairOrderList'),
    path('orders/<int:pk>/', RepairOrder.as_view(), name='repairOrder'),
    path('orders/<int:pk>/repair/<int:pk>/', Repair.as_view(), name='repair'),
]