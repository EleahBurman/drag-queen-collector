from django.forms import ModelForm
from .models import Outfit

class OutfitForm(ModelForm):
    class Meta:
        model = Outfit
        fields = ['date', 'clothes', 'wig', 'makeup', 'nails']
