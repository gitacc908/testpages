from django.shortcuts import render, get_object_or_404
from .models import Pages
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
# Create your views here.


def index(request, pagename):
	pagename = '/' + pagename
	pages = get_object_or_404(Pages, link=pagename)
	
	#pages = Pages.objects.get(link=link)
	
	context = {
		'title': pages.title,
		'body': pages.body,
		'date': pages.update_date,
		'page_list': Pages.objects.all(),

	}
	return render(request, 'pages/pages.html', context=context)

def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#assert False
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(cd['subject'],
					  cd['message'],
					  cd.get('email', 'dylan9803@mail.ru'),
					  ['siteowner@example.com'],
					  connection = con
					  )
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'pages/contact.html', 
		{'form': form, 'page_list': Pages.objects.all(),
		'submitted': submitted})