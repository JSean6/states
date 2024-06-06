from django.shortcuts import render
from .models import State

# Create your views here.
def index(request):
    data = State.objects.all()

    return render(request, 'index.html', {'data': data})


