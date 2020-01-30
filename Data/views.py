from django.shortcuts import render
import json
from django.template import RequestContext
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'dataf/mainjsmenu.html')
