from django.urls import path
from .views import *

urlpatterns = [
    path('case-studies/', CaseStudyPortfolio.as_view(), name="CaseStudyPortfolio"),
    path('web-applications/', ApplicationPortfolio.as_view(), name="ApplicationPortfolio"),
    path('case-studies/<int:pk>/', SingleCaseStudy.as_view(), name="SingleCaseStudy"),
    path('web-applications/<int:pk>/', SingleApplication.as_view(), name="SingleApplication"),
]