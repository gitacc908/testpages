from django.urls import path
from .views import index, contact


urlpatterns = [
	#path('', index, name='index'),
	path('', index, {'pagename': ''}, name='home'),
	path('contact', contact, name='contact'),
	path('<str:pagename>', index, name='index'),
	]