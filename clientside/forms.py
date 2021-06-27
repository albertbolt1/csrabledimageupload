from django import forms 
from .models import *
  
class PlantDiseaseForm(forms.ModelForm): 
  
    class Meta: 
        model = PlantDiseaseImage
        fields = ['Image1','Image2','Image3']