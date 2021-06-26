from django.shortcuts import render
from PIL import Image
from numpy import asarray
from .forms import  PlantDiseaseForm
import requests
# Create your views here.



def plantdisease_image_view(request): 
  
    if request.method == 'POST': 
    	form = PlantDiseaseForm(request.POST, request.FILES)
    	if form.is_valid(): 
    		form.save()
    	name1=request.FILES['plantimage1'].name
    	name2=request.FILES['plantimage2'].name
    	name3=request.FILES['plantimage3'].name
    	img1=open("./images/"+name1,'rb')
    	img2=open("./images/"+name2,'rb')
    	img3=open("./images/"+name3,'rb')
    	files= {'plantimage1':img1,'plantimage2':img2,'plantimage3':img3}
    	url = 'https://csrgiftabled.herokuapp.com/upload'
    	b=requests.post(url, files=files)
    	return render(request,'clientside/teja.html',{'b': b.json()})

    else:
    	form=PlantDiseaseForm()
    	return render(request, 'clientside/home.html',{'form':form})
  
