from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib.auth.models import User

def get_current_user(req):
    return User.objects.filter(username=req.user.get_username()).get()

# Create your views here.
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            current_user = get_current_user(request)
            context = {"user": current_user}
            return render(request, "home.html", context=context)
        else:
            return render(request, "home.html", context={})



