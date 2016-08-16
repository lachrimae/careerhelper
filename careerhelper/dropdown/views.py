from django.shortcuts import render
from django.http import HttpResponse

from .jsonist import getJSON

@require_GET()
def json(request, majorcode, remainder):
    code = majorcode + remainder
    return HttpResponse(getJSON(code))

# Create your views here.
