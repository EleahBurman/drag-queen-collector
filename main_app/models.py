from django.db import models
from django.urls import reverse
from datetime import date

class Performance(models.Model):
  venue = models.CharField(max_length=100, default='Heart')
  date = models.DateField(default=date.today)
  website = models.URLField(default='https://www.heartweho.com/', blank=True, null=True)
  
  def __str__(self):
    return f"Performance at {self.venue} on {self.date}"
  
  def get_absolute_url(self):
        return reverse('performance-detail', kwargs={'pk': self.id})
  
class DragQueen(models.Model):
  name = models.CharField(max_length=100)
  season = models.IntegerField()
  winner = models.BooleanField(default=False)
  allstars = models.IntegerField(null=True, blank=True, default=0)
  winnerofallstars = models.BooleanField(default=False)
  specialty = models.CharField(max_length=250)
  instagramhandle = models.CharField(max_length=100)
  
  def is_dressed_for_today(self):
    today = date.today()
    has_outfit = self.outfit_set.get(date=today)
    if has_outfit:
      return f"{self.name} is dressed and ready to impress today!"
    else:
      return f"{self.name} needs an outfit for today!"
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("dragqueen_detail", kwargs={"dragqueen_id": self.id})
    
class Outfit(models.Model):
  date = models.DateField(default=date.today)
  clothes = models.CharField(max_length=100, default='Body Suit')
  wig = models.CharField(max_length=100, default= 'Teased Blonde Wig')
  makeup = models.CharField(max_length=100, default='Winged Eyeliner')
  nails = models.BooleanField(default=False)
  
  dragqueen = models.ForeignKey(DragQueen, on_delete=models.CASCADE)
  
def __str__(self):
    return f"{self.dragqueen} wore {self.clothes} and {self.wig} and {self.makeup} and {self.nails} on {self.date}"
  
class Meta:
    ordering = ['-date']
  