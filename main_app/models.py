from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User

CLOTHES_CHOICES = (
  ('Reveal Coat', 'Reveal Coat'),
  ('Blue Ostrich Feather Dress', 'Blue Ostrich Feather Dress'),
  ('Little Black Dress', 'Little Black Dress'),
  ('Magenta Body Suit', 'Magenta Body Suit'),
  ('Cheetah Dress', 'Cheetah Dress'),
  ('Transparent Neon Yellow Dress', 'Transparent Neon Yellow Dress'),
  ('Silver Goddess Dress', 'Silver Goddess Dress'),
  ('Mesh Corset Dress', 'Mesh Corset Dress'),
  ('Puff Sleeve Leopard Jacket', 'Puff Sleeve Leopard Jacket'),
  ('Red Hologram Jacket', 'Red Hologram Jacket'),
  ('Silver Sequin Dress', 'Silver Sequin Dress'),
)

WIG_CHOICES = (
    ('Brunette A-Line Bob', 'Brunette A-Line Bob'),
    ('Blonde A-Line Bob', 'Blonde A-Line Bob'),
    ('Black A-Line Bob', 'Black A-Line Bob'),
    ('Red A-Line Bob', 'Red A-Line Bob'),
    ('Pink A-Line Bob', 'Pink A-Line Bob'),
    ('Purple A-Line Bob', 'Purple A-Line Bob'),
    ('Brunette Blunt Bob', 'Brunette Blunt Bob'),
    ('Blonde Blunt Bob', 'Blonde Blunt Bob'),
    ('Black Blunt Bob', 'Black Blunt Bob'),
    ('Red Blunt Bob', 'Red Blunt Bob'),
    ('Pink Blunt Bob', 'Pink Blunt Bob'),
    ('Purple Blunt Bob', 'Purple Blunt Bob'),
    ('Brunette Straight Sleek Bob', 'Brunette Straight Sleek Bob'),
    ('Blonde Straight Sleek Bob', 'Blonde Straight Sleek Bob'),
    ('Black Straight Sleek Bob', 'Black Straight Sleek Bob'),
    ('Red Straight Sleek Bob', 'Red Straight Sleek Bob'),
    ('Pink Straight Sleek Bob', 'Pink Straight Sleek Bob'),
    ('Purple Straight Sleek Bob', 'Purple Straight Sleek Bob'),
    ('Brunette Long Straight Hair', 'Brunette Long Straight Hair'),
    ('Blonde Long Straight Hair', 'Blonde Long Straight Hair'),
    ('Black Long Straight Hair', 'Black Long Straight Hair'),
    ('Red Long Straight Hair', 'Red Long Straight Hair'),
    ('Pink Long Straight Hair', 'Pink Long Straight Hair'),
    ('Purple Long Straight Hair', 'Purple Long Straight Hair'),
    ('Brunette Bangs', 'Brunette Bangs'),
    ('Blonde Bangs', 'Blonde Bangs'),
    ('Black Bangs', 'Black Bangs'),
    ('Red Bangs', 'Red Bangs'),
    ('Pink Bangs', 'Pink Bangs'),
    ('Purple Bangs', 'Purple Bangs'),
    ('Brunette Pixie', 'Brunette Pixie'),
    ('Blonde Pixie', 'Blonde Pixie'),
    ('Black Pixie', 'Black Pixie'),
    ('Red Pixie', 'Red Pixie'),
    ('Pink Pixie', 'Pink Pixie'),
    ('Purple Pixie', 'Purple Pixie'),
)

MAKEUP_CHOICES = (
  ('mascara', 'Mascara'),
  ('Face Primer', 'Face Primer'),
  ('Foundation', 'Foundation'),
  ('Highlighter', 'Highlighter'),
  ('Glue Stick', 'Glue Stick'),
  ('Red Eye Shadow', 'Red Eye Shadow'),
  ('Orange Eye Shadow', 'Orange Eye Shadow'),
  ('Yellow Eye Shadow', 'Yellow Eye Shadow'),
  ('Green Eye Shadow', 'Green Eye Shadow'),
  ('Blue Eye Shadow', 'Blue Eye Shadow'),
  ('Purple Eye Shadow', 'Purple Eye Shadow'),
  ('Eyeliner', 'Eyeliner'),
  ('Translucent Powder', 'Translucent Powder'),
  ('False Lashes', 'False Lashes'),
  ('Lip Liner', 'Lip Liner'),
  ('Red Lipstick', 'Red Lipstick'),
  ('Pink Lipstick', 'Pink Lipstick'),
  ('Black Lipstick', 'Black Lipstick'),
  ('Clear Gloss', 'Clear Gloss'),
  ('Pink Gloss', 'Pink Gloss'),
  ('Red Gloss', 'Red Gloss'),
  ('Blush', 'Blush'),
  ('Bronzer', 'Bronzer'),
)
def get_default_date():
    return 'Click Here'
  
class Performance(models.Model):
  show = models.CharField(max_length=200, default='Planet Pride')
  venue = models.CharField(max_length=100, default='Heart')
  date = models.DateField('Date', default=get_default_date)
  time = models.CharField(default='8pm',max_length=10)
  website = models.URLField(default='https://www.heartweho.com/', blank=True, null=True)

  def get_time_as_datetime(self):
    hour, minute = map(int, self.time[:-2].split(':'))
    if self.time.lower().endswith('pm') and hour < 12:
      hour += 12
      return datetime.time(hour=hour, minute=minute)
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
  performances = models.ManyToManyField(Performance)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("dragqueen_detail", kwargs={"dragqueen_id": self.id})
  
  def is_dressed_for_today(self):
    return self.outfit_set.filter(date=date.today()).exists()
  
class Outfit(models.Model):
    date = models.DateField('Date',  default=get_default_date)
    clothes = models.CharField(
      max_length=100, 
      choices=CLOTHES_CHOICES,
      default=CLOTHES_CHOICES[0][0],
      blank=True, 
      null=True
    )
    wig = models.CharField(
      max_length=100, 
      choices=WIG_CHOICES,
      default=WIG_CHOICES[0][0],
      blank=True, 
      null=True
      )
    makeup = models.CharField(
      max_length=100, 
      choices=MAKEUP_CHOICES,
      default=MAKEUP_CHOICES[0][0],
      blank=True, 
      null=True
    )
    nails = models.BooleanField(default=False)
  
    dragqueen = models.ForeignKey(DragQueen, on_delete=models.CASCADE)
  
    def __str__(self):
        return f"{self.dragqueen} wore {self.clothes} and {self.wig} on {self.date}"
  
    class Meta:
        ordering = ['-date']
  