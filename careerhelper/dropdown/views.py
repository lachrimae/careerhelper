from django.shortcuts import render
from django.http import HttpResponse

import careerapp.models as app

@require_GET()
def json(request, majorcode, remainder):
    code = majorcode + remainder


# Create your views here.
