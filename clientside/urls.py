from django.urls import path,include
from . import views
from django.conf.urls import url
app_name = 'measure'
urlpatterns = [
	path('', views.home, name = 'home'),
	path('handsplint/', views.handsplint, name = 'handsplint'),
	path('standingframe/', views.standingframe, name = 'standingframe'),
	path('walker/', views.walker, name = 'walker')
]
