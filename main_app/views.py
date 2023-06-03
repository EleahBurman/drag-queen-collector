from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Queen

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dragqueen_index(request):
  dragqueens = Queen.objects.all()
  return render(request, 'dragqueens/index.html', {'dragqueens': dragqueens })

def dragqueen_detail(request, dragqueen_id):
  dragqueen = Queen.objects.get(id=dragqueen_id)
  return render(request, 'dragqueens/detail.html', {'dragqueen': dragqueen})

class QueenCreate(CreateView):
  model = Queen
  fields = ['name', 'season', 'winner', 'allstars', 'winnerofallstars', 'specialty', 'instagramhandle']
  success_url = '/dragqueens/'
  
class QueenUpdate(UpdateView):
  model = Queen
  fields = ['season', 'winner', 'allstars', 'winnerofallstars', 'specialty', 'instagramhandle'] 
  
class QueenDelete(DeleteView):
  model = Queen
  success_url = '/dragqueens/'