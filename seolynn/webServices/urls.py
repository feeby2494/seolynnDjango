from django.urls import path
from .views import *

urlpatterns = [
    path('submit_one_project/', OrderSubmitSingleProject.as_view(), name="OrderSubmitSingleProject"),
    path('submit_multi_project/', OrderSubmitMultiProjects.as_view(), name="OrderSubmitMultiProjects"),
    path('<str:username>/orders_all/', OrdersAll.as_view(), name="OrdersAll"),
    path('<str:username>/projects_all/', ProjectsAll.as_view(), name="ProjectsAll"),
    path('<str:username>/<slug:work_order_slug>/', ProjectsForOneOrder.as_view(), name="ProjectsForOneOrder"),
    path('<str:username>/<int:order_id>/<int:project_id>/', ProjectSingle.as_view(), name="ProjectSingle"),
]