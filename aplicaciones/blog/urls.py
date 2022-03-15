from django.urls import path
from .views import *

urlpatterns =  [
	path('',home, name = 'index'),
	path('generales/',generales, name = 'generales'),
	path('elementos_pasivos/',elementos_pasivos, name = 'elementos_pasivos'),
	path('elementos_activos/',elementos_activos, name = 'elementos_activos'),
	path('<slug:slug>/',detallePost, name ='detalle_post'),

]