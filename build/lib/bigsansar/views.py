import datetime
import os
from bigsansar.contrib.advance.models import css, javascript
from www.settings import BASE_DIR
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from bigsansar.contrib.sites.models import domains, pages

DEFAULT_TEMPLATE = 'default.html'


def index(request):
    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        total = db.visitor + 1
        domains.objects.filter(pk=db.id).update(visitor=total)


    except:
        current_site = get_current_site(request)
        time = datetime.datetime.now()
        return render(request, 'parking.html', {'domain': current_site, 'time': time})

    else:
        asp = 'templates/' + str(db.domain) + '/' + 'index.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, DEFAULT_TEMPLATE))
            
        return HttpResponse(template.render({'gethost': db}, request))


def pathviews(request, url):
    default_page = 'defaultpage.html'

    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        get_pagename = url.strip('/')
        page = pages.objects.get(domain=db, slug=get_pagename)
        total = db.visitor + 1
        pagetotal = page.visitor + 1
        domains.objects.filter(pk=db.id).update(visitor=total)
        pages.objects.filter(domain=db, slug=get_pagename).update(visitor=pagetotal)

    except:

        return render(request, '404.html')

    else:
        asp = 'templates/' + str(db.domain) + '/' + page.slug + '.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, default_page))
        return HttpResponse(template.render({'gethost': db, 'getpage': page}, request))


def getcss(request):
    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        get_css = css.objects.get(domain = db)
    except:

        return render(request, '404.html')
    
    else:

        gethttp = HttpResponse(get_css.css)
        gethttp['Content-Type'] = 'text/css'
        return gethttp
    

def getjavascript(request):
    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        get_javascript = javascript.objects.get(domain = db)
    except:
        return render(request, '404.html')
    
    else:

        getjavahttp = HttpResponse(get_javascript.javascript)
        getjavahttp['Content-Type'] = 'text/javascript'
        return getjavahttp