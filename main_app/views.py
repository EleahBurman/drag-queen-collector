from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Drag Queen Collector</h1>')

def about(request):
  return render(request, 'about.html')