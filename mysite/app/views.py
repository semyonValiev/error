from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
def index(request):
    return render(request,"index.html")

class index2(TemplateView):
    template_name = "index2.html"