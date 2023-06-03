from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dragqueens/', views.dragqueen_index, name='dragqueen-index'),
  path('dragqueens/<int:dragqueen_id>/', views.dragqueen_detail, name='dragqueen-detail'),
  path('dragqueens/create/', views.QueenCreate.as_view(), name='dragqueen-create')
]