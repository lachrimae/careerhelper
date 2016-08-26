from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from careerapp.models import MajorGroup

# Create your views here.

def src_resolver(request, ):
    return HttpResponseRedirect

def homepage_redirect(request):
    return HttpResponseRedirect("/app/")

def homepage(request):
    context = { 'majorgroups': MajorGroup.objects.all() }
    return render(request, 'careerapp/homepage.html', context)

def test(request):
    return HttpResponse("You did it!")

#def homepage(request):
    """
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/results/')
    else:
        form = NameForm()
    return render(request, 'homepage.html', {'form': form})
    """
#    return django.http.HttpResponse("Hello there. You've found the recommender page.")
