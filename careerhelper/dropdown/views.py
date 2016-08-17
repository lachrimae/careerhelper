from django.shortcuts import render
from django.http import HttpResponse

import careerapp.models as app

from .jsonist import getJSON

@require_GET()
def json(request, majorcode, remainder):
    code = majorcode + "-" + remainder
    return HttpResponse(getJSON(group))

@require_GET()
def majorgroups(request):
    return HttpResponse(getJSON('majorgroups'))

# Create your views here.
