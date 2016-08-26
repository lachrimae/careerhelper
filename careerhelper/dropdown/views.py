from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET

import careerapp.models as app

from .jsonist import getJSON

@require_GET
def json(request, majorcode, remainder):
    code = majorcode + "-" + remainder
    try:
        response = getJSON(code)
    except:
        raise Http404("SOC Entity " + code + " does not exist.")
    return HttpResponse(response)

@require_GET
def majorgroups(request):
    return HttpResponse(getJSON('majorgroups'))

# Create your views here.
