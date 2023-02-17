from audioop import reverse
from django.http import HttpResponseNotFound
from django.urls import reverse

def handler404(request, exception):
    page_not_found = exception.args[0]['path']
    return HttpResponseNotFound(f"<div><h3>Error 404: </h4> <h5>Sorry, the page: {page_not_found} deos not exist!</h5> <a href='{reverse('home')}'><button>Back to Homepage</button></a></div>")