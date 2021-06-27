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
    	name1=request.FILES['Image1'].name
    	name2=request.FILES['Image2'].name
    	name3=request.FILES['Image3'].name
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



def home(request):
	return render(request,'clientside/Homepage.html')


def handsplint(request):
	form=PlantDiseaseForm()
	if request.method == 'POST': 
		form = PlantDiseaseForm(request.POST, request.FILES)
		if form.is_valid(): 
			form.save()
		name1=request.FILES['Image1'].name
		name2=request.FILES['Image2'].name
		name3=request.FILES['Image3'].name
		img1=open("./images/"+name1,'rb')
		img2=open("./images/"+name2,'rb')
		img3=open("./images/"+name3,'rb')
		files= {'plantimage1':img1,'plantimage2':img2,'plantimage3':img3}
		url = 'https://csrgiftabled.herokuapp.com/upload'
		b=requests.post(url, files=files)
		c=b.json()["measures"]
		e={'handcrease':c[6]*100,'tiptomid':c[7]*100 ,'armtowrist':c[5]*100}
		return render(request,'clientside/Submit_Page.html',{'e':e})
	else:
		form=PlantDiseaseForm()
		return render(request,'clientside/Hand_Splint.html',{'form':form})



def standingframe(request):
	form=PlantDiseaseForm()
	if request.method == 'POST': 
		form = PlantDiseaseForm(request.POST, request.FILES)
		if form.is_valid(): 
			form.save()
		name1=request.FILES['Image1'].name
		name2=request.FILES['Image2'].name
		name3=request.FILES['Image3'].name
		img1=open("./images/"+name1,'rb')
		img2=open("./images/"+name2,'rb')
		img3=open("./images/"+name3,'rb')
		files= {'plantimage1':img1,'plantimage2':img2,'plantimage3':img3}
		url = 'https://csrgiftabled.herokuapp.com/upload'
		b=requests.post(url, files=files)
		c=b.json()["measures"]
		e={'headtoheel':c[0]*100,'elbowtoheel':c[1]*100 ,'hiptohip':c[2]*100,'kneetoheel':c[3]*100,'umbilicaltoheel':c[4]*100 ,'hiptoheel':c[4]*100}
		return render(request,'clientside/Submit_Page.html',{'e':e})
	else:
		form=PlantDiseaseForm()
		return render(request,'clientside/Standing_frame.html',{'form':form})



def walker(request):
	form=PlantDiseaseForm()
	if request.method == 'POST': 
		form = PlantDiseaseForm(request.POST, request.FILES)
		if form.is_valid(): 
			form.save()
		name1=request.FILES['Image1'].name
		name2=request.FILES['Image2'].name
		name3=request.FILES['Image3'].name
		img1=open("./images/"+name1,'rb')
		img2=open("./images/"+name2,'rb')
		img3=open("./images/"+name3,'rb')
		files= {'plantimage1':img1,'plantimage2':img2,'plantimage3':img3}
		url = 'https://csrgiftabled.herokuapp.com/upload'
		b=requests.post(url, files=files)
		c=b.json()["measures"]
		e={'floortohip':c[5]*100,'floortowrist':c[8]*100}
		return render(request,'clientside/Submit_Page.html',{'e':e})
	else:
		form=PlantDiseaseForm()
		return render(request,'clientside/walker.html',{'form':form})


  
