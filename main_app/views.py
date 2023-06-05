from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DragQueen, Performance
from .forms import OutfitForm

class PerformanceCreate(CreateView):
  model = Performance
  fields = '__all__'
  
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dragqueen_index(request):
  dragqueens = DragQueen.objects.all()
  return render(request, 'dragqueens/index.html', {'dragqueens': dragqueens })

def dragqueen_detail(request, dragqueen_id):
  dragqueen = DragQueen.objects.get(id=dragqueen_id)
  outfit_form = OutfitForm()
  return render(request, 'dragqueens/detail.html', {
    'dragqueen': dragqueen, 'outfit_form': outfit_form})

def add_outfit(request, dragqueen_id):
    if request.method == 'POST':
        form = OutfitForm(request.POST)
        if form.is_valid():
            new_outfit = form.save(commit=False)
            dragqueen = DragQueen.objects.get(id=dragqueen_id)
            new_outfit.dragqueen = dragqueen
            new_outfit.save()
            return redirect('dragqueen-detail', dragqueen_id=dragqueen_id)
    else:
        form = OutfitForm()
    
    return render(request, 'add_outfit.html', {'form': form})


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