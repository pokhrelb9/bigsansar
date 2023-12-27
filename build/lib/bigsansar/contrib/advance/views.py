import json
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.core.paginator import Paginator
import requests
from bigsansar.contrib.advance.forms import chpassform, custom_admin_upadte, loginform, profileform, userchform, usrinfoform
from bigsansar.contrib.advance.models import admin_update
from bigsansar.contrib.sites.models import domains
from django.contrib import messages


# Create your views here.
def admin_redirect(request):
    return redirect('admin/')


@csrf_exempt
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('/admin/dashboard')
    else:
        if request.method == "POST":
            fm = loginform(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/admin/dashboard')

        else:
            fm = loginform()
        return render(request, 'admin/login.html', {'form': fm})
    

def userlogout(request):
    logout(request)
    return redirect('/admin')


def dashboard(request):
    if request.user.is_authenticated:

        user = request.user
        getdomain = domains.objects.filter(user=user).order_by('-id')
        paginator = Paginator(getdomain, 5)
        page_number = request.GET.get('page')
        domain = paginator.get_page(page_number)
        ip = request.META.get('REMOTE_ADDR')
        res = requests.get('http://ip-api.com/json/'+ip)
        location_data_one = res.text
        geo = json.loads(location_data_one)
        browser = request.META['HTTP_USER_AGENT']
        update = admin_update.objects.all().order_by('-id')[:5]
        return render(request, 'admin/dashboard.html', {'blog': update, 'ip': ip, 'geo': geo, 'browser': browser,
                                                  'domains': domain, })

    else:
        return redirect('/admin')
    


def chuname(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = userchform(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Username Changed Successfully')
                return redirect('/admin/dashboard')

        else:
            fm = userchform(instance=request.user)
        return render(request, 'admin/chuname.html', {'form': fm})
    else:
        return redirect('/admin')
    

def chpass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = chpassform(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Changed Successfully')
                return redirect('/admin/dashboard')
        else:
            form = chpassform(user=request.user)
        return render(request, 'admin/chpass.html', {'form': form})

    else:
        return redirect('/admin')
    

def editprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = profileform(request.POST, instance=request.user)
            form1 = usrinfoform(request.POST, instance=request.user.userinfo)
            if form.is_valid() and form1.is_valid():
                form.save()
                form1.save()
                messages.success(request, 'Profile Successfully Updated')
                return redirect('/admin/dashboard')

        else:
            form = profileform(instance=request.user)
            form1 = usrinfoform(instance=request.user.userinfo)
        return render(request, 'admin/editprofile.html', {'form': form, 'form1': form1})

    else:
        return redirect('/admin')
    


def admin_update_fun(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                form = custom_admin_upadte(request.POST)
                if form.is_valid():
                    q = form.save(commit=False)
                    q.user = request.user
                    q.save()
                    messages.success(request, 'admin updated Successfully Created')
                    return redirect('/admin/dashboard')

            else:
                form = custom_admin_upadte()
            return render(request, 'admin/admin_update.html', {'form': form,})

        else:
            return render(request, '404.html')

    else:
        return redirect('/login')