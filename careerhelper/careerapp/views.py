from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#from .forms import CareerForm

# Create your views here.

def homepage_redirect(request):
    return HttpResponseRedirect("/app/")

def homepage(request):
    return HttpResponse("Hello there. You've found the recommender page.")

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
