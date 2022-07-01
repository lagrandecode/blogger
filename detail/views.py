from multiprocessing import context
from django.shortcuts import render
from detail.models import Detail

# Create your views here.

def index(request):
    detail = Detail.objects.all()
    context = {
        "detail" : detail
    }
    return render(request, "index.html", context)
