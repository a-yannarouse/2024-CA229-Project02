# \simple_test_root\pages\views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.http import Http404
from . models import Page
from .contact import ContactForm

def index(request, pagename = ''):
    print('Pagename: ' + pagename)
    try:                            # Indent the next set of lines
        pagename = '/' + pagename
        pg = Page.objects.get(permalink=pagename)
        context = {
            'title': pg.title,
            'content': pg.bodytext,
            'last_updated': pg.update_date,
            'page_list': Page.objects.all(),
            'pic': pg.pic,
        }
        return render(request, 'Genres/base.html', context)
    except:
        raise Http404("No model matches the given query.")