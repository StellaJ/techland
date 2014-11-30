from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import PersonForm
from models import Person


def home(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return HttpResponseRedirect('/techsite/home/')
    else:
        form = PersonForm()
        list_people = Person.objects.all()
        context = {'list_people' : list_people, 'form': form }
    return render(request, 'home.html', context )

# Create your views here.