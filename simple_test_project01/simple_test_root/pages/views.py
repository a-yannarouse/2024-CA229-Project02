# \simple_test_root\pages\views.py
from django.shortcuts import render
# from django.http import HttpResponse
from . models import Page
from datetime import date # Add this line near top of file


def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    t = date.today()
    month = t.strftime('%b')
    year = t.year
    context = {
    	'title': pg.title,
    	'content': pg.bodytext,
        'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
	    'welcome': f'Welcome to {month} {year}',
    }
    return render(request, 'pages/page.html', context)
