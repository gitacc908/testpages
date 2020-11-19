from django.urls import path
from .views import quote_req, Quote_list, QuoteDetail

urlpatterns = [
	path('', quote_req, name='quote-req'),
	path('show/', Quote_list.as_view(), name='quote_list'),
	path('show/<int:pk>', QuoteDetail.as_view(), name='quote_detail'),
]