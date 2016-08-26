from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CareerForm

def get_recommendation(request)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/results/')

    else:
        form = NameForm()

return render(request, 'homepage.html', {'form': form})
