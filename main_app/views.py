from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Drag Queen Collector</h1>')

def about(request):
  return render(request, 'about.html')

class Queen:
  def __init__(self, name, season, winner, allstars, winnerofallstars, specialty, instagramhandle):
    self.name = name
    self.season = season
    self.winner = winner
    self.allstars = allstars
    self.winnerofallstars = winnerofallstars
    self.specialty = specialty
    self.instagramhandle = instagramhandle

dragqueens = [
  Queen('Katya', 7, False, 2, False, 'Splits', 'katya_zamo')
]

def dragqueen_index(request):
  return render(request, 'dragqueens/index.html', {'dragqueens': dragqueens })