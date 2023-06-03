from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dragqueens/', views.dragqueen_index, name='dragqueen-index'),
  path('dragqueens/<int:dragqueen_id>/', views.dragqueen_detail, name='dragqueen-detail'),
  path('dragqueens/create/', views.DragQueenCreate.as_view(), name='dragqueen-create'),
  path('dragqueens/<int:pk>/update/', views.DragQueenUpdate.as_view(), name='dragqueen-update'),
  path('dragqueens/<int:pk>/delete/', views.DragQueenDelete.as_view(), name='dragqueen-delete'),
  path('dragqueens/<int:dragqueen_id>/add-outfit/', views.add_outfit, name='add-outfit'),
  
]