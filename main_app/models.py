from django.db import models
from django.urls import reverse

# Create your models here.
class Queen(models.Model):
  name = models.CharField(max_length=100)
  season = models.IntegerField()
  winner = models.BooleanField(default=False)
  allstars = models.IntegerField(null=True, blank=True, default=0)
  winnerofallstars = models.BooleanField(default=False)
  specialty = models.CharField(max_length=250)
  instagramhandle = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("dragqueen_detail", kwargs={"dragqueen_id": self.id})
  