from django.shortcuts import render
from .models import Queen

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dragqueen_index(request):
  dragqueens = Queen.objects.all()
  return render(request, 'dragqueens/index.html', {'dragqueens': dragqueens })