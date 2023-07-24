import json
import os
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
import requests
from bigsansar.contrib.sites.forms import create_domainform, customviewseditpage, customviewspageform
from django.contrib import messages
from bigsansar.contrib.sites.models import domains, pages
from django.utils.text import slugify
from django.core.exceptions import ValidationError

from www.settings import BASE_DIR

# Create your views here.


def manage_domain(request, id):
    if request.user.is_authenticated:

        try:
            ruser = request.user
            query = domains.objects.get(id=id, user=ruser)

        except:

            return render(request, '404.html')

        else:
            status = query.visitor
            if status == 0:
                visitor = 'Deactive'

            else:
                visitor = 'Active'

            getpage = pages.objects.filter(domain=id).order_by('-id')
            paginator = Paginator(getpage, 5)
            page_number = request.GET.get('page')
            page = paginator.get_page(page_number)
            ip = request.META.get('REMOTE_ADDR')
            res = requests.get('http://ip-api.com/json/' + ip)
            location_data_one = res.text
            geo = json.loads(location_data_one)
            browser = request.META['HTTP_USER_AGENT']
            update = None
            #admin_update.objects.all().order_by('-id')[:5]
            return render(request, 'admin/domain_manage.html', {'visitcount': status, 'count': visitor, 'host': query,
                                                          'pages': page, 'ip': ip, 'geo': geo, 'browser': browser,
                                                          'blog': update})
    else:
        return redirect('/admin')
    


def edit_host(request, id):

    if request.user.is_authenticated:

        try:
            user = request.user
            query = domains.objects.get(id=id, user=user)

        except:
            return render(request, '404.html')

        else:
            if request.method == 'POST':
                form = create_domainform(request.POST, instance=query)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Domain Successfully Updated')
                    return redirect('/admin/domain/manage/' + id)
            else:
                form = create_domainform(instance=query)
            return render(request, 'admin/edit_domain.html', {'form': form})

    else:
        return redirect('/login')



def page_create(request, id):
    if request.user.is_authenticated:
        try:
            user = request.user
            get_host = domains.objects.get(pk=id, user=user)

        except:
            return render(request, '404.html')

        getdir = 'templates'
        if request.method == 'POST':
            form = customviewspageform(request.POST)
            if form.is_valid():

                if pages.objects.filter(slug=slugify(form.cleaned_data.get('title')), domain=get_host):
                    messages.warning(request, 'page with url' + ' ' + slugify(
                        form.cleaned_data.get('title')) + ' ' + 'already exists for domain' + ' ' + get_host.domain)
                    form = customviewspageform
                    return render(request, 'admin/page_create.html', {'form': form})

                query = form.save(commit=False)
                query.domain = get_host
                query.slug = slugify(form.cleaned_data.get('title'))
                mkdir = getdir + '/' + str(get_host.domain)

                try:
                    final_directory = os.path.join(BASE_DIR, mkdir)
                    if not os.path.exists(final_directory):
                        os.makedirs(final_directory)
                except:
                    raise ValidationError(
                        _(final_directory + ' Directory not created "Permission Denied"'),
                    )

                query.save()

                messages.success(request, 'Pages Successfully Created')
                return redirect('/admin/domain/manage/' + id)

        else:
            form = customviewspageform
        return render(request, 'admin/page_create.html', {'form': form})

    else:
        return redirect('/admin')



def pages_edit(request, id, pagesid):
    if request.user.is_authenticated:
        getdir = 'templates'

        try:
            user = request.user
            get_host = domains.objects.get(pk=id, user=user)
            query = pages.objects.get(domain=id, id=pagesid)

        except:
            return render(request, '404.html')

        else:
            if request.method == 'POST':
                form = customviewseditpage(request.POST, instance=query)
                if form.is_valid():
                    db = form.save(commit=False)
                    db.domain = get_host

                    mkdir = getdir + '/' + str(get_host.domain)
                    full_path = os.path.join(BASE_DIR, mkdir)
                    createfile = full_path + '/' + query.slug + '.html'
                    get_content = form.cleaned_data.get('body')

                    f = open(createfile, "w", encoding="utf-8")
                    f.write(get_content)
                    f.close()
                    db.save()
                    messages.success(request, 'pages Successfully Updated')
                    return redirect('/admin/domain/manage/' + id)

            else:
                form = customviewseditpage(instance=query)

            return render(request, 'admin/page_edit.html', {'form': form})

    else:

        return redirect('/admin')



def page_delete(request, id, pagesid):
    if request.user.is_authenticated:
        getdir = 'templates'

        try:
            user = request.user
            getdomain = domains.objects.get(pk=id, user=user)
            query = pages.objects.get(domain=id, id=pagesid)

        except:
            return render(request, '404.html')

        if request.method == 'POST':
            mkdir = getdir + '/' + str(getdomain.domain)
            createfile = mkdir + '/' + query.slug + '.html'

            if os.path.exists(createfile):
                os.remove(createfile)
                query.delete()
            else:
                query.delete()

            messages.success(request, 'Pages Successfully Deleted')
            return redirect('/admin/domain/manage/' + id)
        return render(request, 'admin/page_delete.html', {'path': query, 'domain': getdomain})

    else:
        redirect('/admin')