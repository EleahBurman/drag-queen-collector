from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DragQueen

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dragqueen_index(request):
  dragqueens = DragQueen.objects.all()
  return render(request, 'dragqueens/index.html', {'dragqueens': dragqueens })

def dragqueen_detail(request, dragqueen_id):
  dragqueen = Queen.objects.get(id=dragqueen_id)
  return render(request, 'dragqueens/detail.html', {'dragqueen': dragqueen})

class DragQueenCreate(CreateView):
  model = DragQueen
  fields = ['name', 'season', 'winner', 'allstars', 'winnerofallstars', 'specialty', 'instagramhandle']
  success_url = '/dragqueens/'
  
class DragQueenUpdate(UpdateView):
  model = DragQueen
  fields = ['season', 'winner', 'allstars', 'winnerofallstars', 'specialty', 'instagramhandle'] 
  
class DragQueenDelete(DeleteView):
  model = DragQueen
  success_url = '/dragqueens/'