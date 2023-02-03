from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView, TemplateView
from .forms import ProjectForm, ProjectFormSet
from .models import  WorkOrder, Project
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def get_current_user(req):
    return User.objects.filter(username=req.user.get_username()).get()


# Create your views here.
# Having a decorator here to force users to login before they
# try filling out the form will help this whole process
class OrderSubmitSingleProject(View):
    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            if request.user.is_authenticated:
                current_user = get_current_user(request)
            # Only for testing! DELETE ME
            if request.user.is_anonymous:
                current_user = User.objects.filter(username="jlynn").get()
            
            # new_order = Order.objects.create(slug = f"temp", customer = current_customer)
            new_order = WorkOrder.objects.create(user = current_user)
            new_order.slug = f"{current_user.get_username()}_order_{str(new_order.date_submitted).replace(' ', '_').replace(':', '_'). replace('+', '_').replace('.', '_').replace('-', '_')}"
            new_order.save()
            new_project.order = new_order
            new_project.slug = new_project.project_name
            new_project.save()
            return HttpResponse('looks good!')
    def get(self, request):
        form = ProjectForm()
        return render(request, 'webOrderSubmitForm.html', {'form' : form})

class OrderSubmitMultiProjects(TemplateView):
    def get(self, request):
        formset = ProjectFormSet()
        context = {"formset": formset}
        return render(request, "workOrderMultiProjectForm.html", context)

    def post(self, *args, **kwargs):
        formset = ProjectFormSet(data=self.request.POST)
        current_user = get_current_user(self.request)
        new_order = WorkOrder.objects.create(user = current_user)
        new_order.slug = f"{current_user.get_username()}_order_{str(new_order.date_submitted).replace(' ', '_').replace(':', '_'). replace('+', '_').replace('.', '_').replace('-', '_')}"
        new_order.save()

        if formset.is_valid():
            formset.instance = new_order
            formset.save()
            return redirect(reverse_lazy("OrderSubmitMultiProjects"))

        context = {
            "formset": formset,
            "order": new_order,
        }

        return render(self.request, "workOrderMultiProjectForm.html", context)

# this seriously deosn't make any sense
# class OrdersAll(ListView):
#     def get(self, request, username):
#         # Get all orders for current user
#         #url: /username/orders_all
#         current_user = get_current_user(request)
#         if current_user.get_username() == username:
#             model = WorkOrder
#             TemplateView = "allOrdersForUser.html"

#             def get_queryset(self):
#                 queryset = super().get_queryset()
#                 return queryset.filter(user=self.request.user)

#         # def get_context_data(self, **kwargs):
#         #     context = super().get_context_data(**kwargs)
#         #     context['username'] = current_user.get_username()
            
#         #     return context

class OrdersAll(View):
    def get(self, request, username):
        current_user = get_current_user(request)
        if current_user.get_username() == username:
            orders = WorkOrder.objects.filter(user = current_user).all()
            username = current_user.get_username()
            context = {"orders": orders, "username": username}
            return render(request, "allOrdersForUser.html", context=context)

class ProjectsAll(View):
    def get(self, request, username):
        current_user = get_current_user(request)
        if current_user.get_username() == username:
            projects = Project.objects.filter(order__user = current_user).all()
            username = current_user.get_username()
            context = {"projects": projects, "username": username}
            return render(request, "allProjectsForUser.html", context=context)
        

class ProjectsForOneOrder(View):
    def get(self, request, username, work_order_slug):
        # Get all projects for a spcific word order for current user
        #url: /username/workorder/
        if request.user.is_authenticated:
            current_user = get_current_user(request)
            order = WorkOrder.objects.filter(slug=work_order_slug).get()
            projects = Project.objects.filter(order__user= current_user, order__slug=work_order_slug).all()
            context = {"projects": projects, "order": order}
            return render(request, "oneOrder.html", context=context)

class ProjectSingle(View):
    def get(self, request, username, order_id, project_id):
        # Get one specific project for a spcific word order for current user
        #url: /username/workorder/project
        if request.user.is_authenticated:
            current_user = get_current_user(request)
            project = Project.objects.filter(id=project_id).get()
            context = {"project": project}
            return render(request, "oneProject.html", context=context)