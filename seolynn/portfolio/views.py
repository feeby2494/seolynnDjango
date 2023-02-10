from email.mime import application
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Application, CaseStudy, Project

class CaseStudyPortfolio(ListView):
    model = CaseStudy
    template_name = 'case_studies_portfolio.html'

class ApplicationPortfolio(ListView):
    model = Application
    template_name = 'application_portfolio.html'

class SingleCaseStudy(DetailView):
    model = CaseStudy
    template_name = 'case_study_single.html'

class SingleApplication(DetailView):
    model = Application
    template_name = 'application_single.html'
