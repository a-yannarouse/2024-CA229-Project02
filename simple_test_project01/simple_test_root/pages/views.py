# \simple_test_root\pages\views.py
from django.shortcuts import render
# from django.http import HttpResponse
from . models import Page


def index(request):
    pg = Page.objects.get(permalink='/')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'base.html', context)

def about(request):
    pg = Page.objects.get(permalink='/kpop')
    context = {
	'title': pg.title,
	'content': pg.bodytext
    }
    return render(request, 'kpop.html', context)