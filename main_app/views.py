from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import DragQueen, Performance
from .forms import OutfitForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def dragqueen_index(request):
  dragqueens = DragQueen.objects.filter(user=request.user)
  return render(request, 'dragqueens/index.html', {'dragqueens': dragqueens })

@login_required
def dragqueen_detail(request, dragqueen_id):
  dragqueen = DragQueen.objects.get(id=dragqueen_id)
  performances_dragqueen_not_performing_at = Performance.objects.exclude(id__in = dragqueen.performances.all().values_list('id'))
  outfit_form = OutfitForm()
  return render(request, 'dragqueens/detail.html', {
    'dragqueen': dragqueen, 'outfit_form': outfit_form, 'performances': performances_dragqueen_not_performing_at})

@login_required
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


class DragQueenCreate(LoginRequiredMixin, CreateView):
  model = DragQueen
  fields = ['name', 'season', 'winner', 'allstars', 'winnerofallstars', 'specialty', 'instagramhandle']
  success_url = '/dragqueens/'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class DragQueenUpdate(LoginRequiredMixin, UpdateView):
  model = DragQueen
  fields = ['season', 'winner', 'allstars', 'winnerofallstars', 'specialty', 'instagramhandle'] 
  
class DragQueenDelete(LoginRequiredMixin, DeleteView):
  model = DragQueen
  success_url = '/dragqueens/'
  
class PerformanceCreate(LoginRequiredMixin, CreateView):
  model = Performance
  fields = '__all__'
  
class PerformanceList(LoginRequiredMixin, ListView):
  model = Performance
  
class PerformanceDetail(LoginRequiredMixin, DetailView):
  model = Performance
  
class PerformanceUpdate(LoginRequiredMixin, UpdateView):
  model = Performance
  fields = ['show', 'venue', 'date', 'time', 'website']
  
class PerformanceDelete(LoginRequiredMixin, DeleteView):
  model = Performance
  success_url = '/performances/'

@login_required  
def assoc_performance(request, dragqueen_id, performance_id):
  DragQueen.objects.get(id=dragqueen_id).performances.add(performance_id)
  return redirect('dragqueen-detail', dragqueen_id=dragqueen_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)