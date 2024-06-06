from django.shortcuts import render
from .models import State, People

# Create your views here.
def index(request):
    data = State.objects.all()

    return render(request, 'index.html', {'data': data})

def people(request):
    dataset = People.objects.all()

    return render(request, 'people.html', {'dataset': dataset})



