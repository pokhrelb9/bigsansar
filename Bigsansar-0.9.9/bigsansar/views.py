import datetime
import os
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
        asp = 'home/' + str(db.user) + '/' + str(current_site) + '/' + 'index.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, DEFAULT_TEMPLATE))

        return HttpResponse(template.render({}, request))


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
        asp = 'home/' + str(db.user) + '/' + str(current_site) + '/' + page.slug + '.html'
        full_url = os.path.join(BASE_DIR, asp)
        template = loader.select_template((full_url, default_page))
        return HttpResponse(template.render({'path': url}, request))
