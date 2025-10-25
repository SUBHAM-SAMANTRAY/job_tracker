from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import JobApplication

def home(request):
    jobs = JobApplication.objects.all()
    return render(request, 'home.html', {'jobs': jobs})
