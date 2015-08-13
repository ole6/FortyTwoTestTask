from django.shortcuts import render
from hello.models import Person


def home(request):
    person = Person.objects.all()[0]
    return render(request, 'home.html', {'person': person})
