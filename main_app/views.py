from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import DragQueen, Performance, Outfit, Photo
from .forms import OutfitForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'eleahdragqueencollector'

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
  form = OutfitForm(request.POST)
  if form.is_valid():
    new_outfit = form.save(commit=False)
    new_outfit.dragqueen_id = dragqueen_id
    new_outfit.save()
  return redirect('dragqueen-detail', dragqueen_id=dragqueen_id)

@login_required
def delete_outfit(request, dragqueen_id, outfit_id):
  instance=Outfit.objects.get(id=outfit_id)
  instance.delete()
  return redirect('dragqueen-detail', dragqueen_id=dragqueen_id)
      
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
  def get_success_url(self):
    return reverse('dragqueen-detail', kwargs={'dragqueen_id': self.object.id})
  
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
      return redirect('dragqueen-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def add_photo(request, dragqueen_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, dragqueen_id=dragqueen_id)
      dragqueen_photo = Photo.objects.filter(dragqueen_id=dragqueen_id)
      if dragqueen_photo.first():
        dragqueen_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('dragqueen-detail', dragqueen_id=dragqueen_id)