from django.db import models

# Create your models here.
class PlantDiseaseImage(models.Model): 
	Image1 = models.ImageField(upload_to='images/')
	Image2 = models.ImageField(upload_to='images/')
	Image3 = models.ImageField(upload_to='images/')