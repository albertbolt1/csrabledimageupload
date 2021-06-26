from django.urls import path,include
from . import views
from django.conf.urls import url 

urlpatterns = [
	url(r'', views.plantdisease_image_view, name='image-upload'),
]
