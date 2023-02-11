from urllib import request
from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
import matplotlib.pyplot as plt
import io
import urllib, base64

class TestMatPlt1(View):
    def get(self, request):
        try:
            plt.plot(range(10))
            fig = plt.gcf()
            buffer = io.BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            string = base64.b64encode(buffer.read())
            uri = urllib.parse.quote(string)
            return render(request, 'test_mat_plt_1.html', {'data': uri})
        except:
            raise Http404