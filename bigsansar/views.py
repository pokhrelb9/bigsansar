import datetime
import os
from www.settings import BASE_DIR
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from bigsansar.contrib.blogs.models import post
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



def get_path_url(request, path, slug):
    default_page = 'defaultpage.html'
    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        get_pagename = path.strip('/')
        page = pages.objects.get(domain=db, slug=get_pagename)
        total = db.visitor + 1
        domains.objects.filter(pk=db.id).update(visitor=total)
        

    except:
        return render(request, '404.html')
    
    else:
         
         asp = 'templates/' + str(db.domain) + '/' + page.slug + '.html'
         full_url = os.path.join(BASE_DIR, asp)
         template = loader.select_template((full_url, default_page))
         return HttpResponse(template.render({'gethost': db, 'getpage': page, 'slug': slug}, request))


def getcss(request):
    default_page = 'styles.html'
    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        page = pages.objects.get(domain=db, slug='styles')

    except:
        return render(request, '404.html')
    
    else:
        asp = 'templates/' + str(db.domain) + '/' + page.slug + '.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, default_page))
        gethttp =  HttpResponse(template.render({}, request))
        gethttp['Content-Type'] = 'text/css'
        return gethttp
    

def getjavascript(request):
    default_page = 'script.html'
    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        page = pages.objects.get(domain=db, slug='script')

    except:
        return render(request, '404.html')
    
    else:
        asp = 'templates/' + str(db.domain) + '/' + page.slug + '.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, default_page))
        getjavahttp =  HttpResponse(template.render({}, request))
        getjavahttp['Content-Type'] = 'text/javascript'
        return getjavahttp
    

def sitemap(request):
    default_page = 'sitemap.html'

    try:
        current_site = get_current_site(request)
        db = domains.objects.get(domain=current_site)
        page = pages.objects.get(domain=db, slug='sitemap')

    except:
        return render(request, '404.html')
    
    else:
        asp = 'templates/' + str(db.domain) + '/' + page.slug + '.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, default_page))
        getsitemaphttp =  HttpResponse(template.render({}, request))
        getsitemaphttp['Content-Type'] = 'application/xml'
        return getsitemaphttp
    

