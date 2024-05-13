import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.core.paginator import Paginator
import requests
from bigsansar.contrib.advance.forms import cf_api_key, cf_hostname, chpassform, custom_admin_upadte, loginform, profileform, userchform, usrinfoform
from bigsansar.contrib.advance.models import admin_update, cloudflare_api
from bigsansar.contrib.sites.models import default_domain, domains
from django.contrib import messages

from www.settings import BASE_DIR

# Create your views here.
def admin_redirect(request):
    return redirect('admin/')


@csrf_exempt
def userlogin(request):
    if request.user.is_authenticated:

        if request.user.is_staff:
           
                    try:
                        get_default_domain = default_domain.objects.get(user=request.user)
                    except:
                        return redirect('/admin/domain/create')
                    else:

                        url_get = "/admin/domain/manage/%s" % (get_default_domain.domain.id)
                        return redirect(url_get)
        else:
            return render(request, '404.html')
 
    else:
        if request.method == "POST":
            fm = loginform(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None and user.is_staff:
                    login(request, user)
                    try:
                        get_default_domain = default_domain.objects.get(user=request.user)
                    except:
                        return redirect('/admin/domain/create')
                    else:

                        url_get = "/admin/domain/manage/%s" % (get_default_domain.domain.id)
                        return redirect(url_get)
                
                else:
                    messages.error(request, "Invalid credentials or you do not have staff access.")

        else:
            fm = loginform()
        return render(request, 'admin/login.html', {'form': fm})
    

def userlogout(request):
    logout(request)
    return redirect('/admin')


def account(request):
    if request.user.is_authenticated:

        if request.user.is_staff:
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
            return render(request, 'admin/account_info.html', {'blog': update, 'ip': ip, 'geo': geo, 'browser': browser,
                                                    'domains': domain, })
        
        else:
            return render(request, '404.html')

    else:
        return redirect('/admin')
    


def chuname(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = request.user
           
            if request.method == 'POST':
                fm = userchform(request.POST, instance=request.user)
                if fm.is_valid():
                    fm.save()
                    messages.success(request, 'Username Changed Successfully')
                    return redirect('/admin/account')

            else:
                fm = userchform(instance=request.user)
            return render(request, 'admin/chuname.html', {'form': fm})
        
        else:
            return render(request, '404.html')
    else:
        return redirect('/admin')
    

def chpass(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = request.user
            

            if request.method == 'POST':
                form = chpassform(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                    messages.success(request, 'Password Changed Successfully')
                    return redirect('/admin/account')
            else:
                form = chpassform(user=request.user)
            return render(request, 'admin/chpass.html', {'form': form})
        
        else:
            return render(request, '404.html')

    else:
        return redirect('/admin')
    

def editprofile(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = request.user
           

            if request.method == 'POST':
                form = profileform(request.POST, instance=request.user)
                form1 = usrinfoform(request.POST, instance=request.user.userinfo)
                if form.is_valid() and form1.is_valid():
                    form.save()
                    form1.save()
                    messages.success(request, 'Profile Successfully Updated')
                    return redirect('/admin/account')

            else:
                form = profileform(instance=request.user)
                form1 = usrinfoform(instance=request.user.userinfo)
            return render(request, 'admin/editprofile.html', {'form': form, 'form1': form1})
        
        else:
            return render(request, '404.html')

    else:
        return redirect('/admin')
    


def admin_update_fun(request):

    if request.user.is_authenticated:
        if request.user.is_superuser:
           
            

            if request.method == 'POST':
                form = custom_admin_upadte(request.POST)
                if form.is_valid():
                    q = form.save(commit=False)
                    q.user = request.user
                    q.save()
                    messages.success(request, 'admin updated Successfully Created')
                    return redirect('/admin')

            else:
                form = custom_admin_upadte()
            return render(request, 'admin/admin_update.html', {'form': form})

        else:
            return render(request, '404.html')

    else:
        return redirect('/login')
    

def cloudflare(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            try:
                query = cloudflare_api.objects.latest('id')
                get_zone_id = domains.objects.get(domain=query.main_domain_name).zone_id
                
                headers = {
                        'Content-Type': 'application/json',
                        'X-Auth-Email': query.email,
                        'X-Auth-Key': query.global_api_key
                    }
                
                url = f'https://api.cloudflare.com/client/v4/zones/{get_zone_id}'
                ssl_url = f"https://api.cloudflare.com/client/v4/zones/{get_zone_id}/settings/ssl"
                

                response = requests.get(url, headers=headers)
                response_for_ssl = requests.get(ssl_url, headers=headers)
                    # Handle the response
                if response.status_code == 200:
                    if response_for_ssl.status_code == 200:
                        get_ssl_status = response_for_ssl.json()['result']['value']

                    else:
                        return JsonResponse({'error': 'Failed to retrieve Cloudflare SSL/TLS encryption mode.'}, status=500)
                    
                    ns = response.json()['result']['name_servers']
                    return render(request, 'admin/cloudflare.html', {'cf': query, 'ssl_value': get_ssl_status, 'status': response.json()['result']['status'], 'name_servers1': ns[0], 'name_servers2': ns[1]})
                else:
                    return render(request, 'admin/db_cloudflare.html')
            except:
                return render(request, 'admin/db_cloudflare.html')
            
        else:
            return render(request, '404.html')
    
    else:
        return redirect('/login')
    

def cf_conf(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            form_title = 'Cloudflare Authentigration'
            user = request.user
            
            if request.method == 'POST':
                form = cf_api_key(request.POST)
                if form.is_valid():
                    api_key = form.cleaned_data['global_api_key']
                    email = form.cleaned_data['email']
                     # Make a request to the Cloudflare API
                    headers = {
                        'Content-Type': 'application/json',
                        'X-Auth-Email': email,
                        'X-Auth-Key': api_key
                    }
                    url = 'https://api.cloudflare.com/client/v4/zones'

                    response = requests.get(url, headers=headers)
                    # Handle the response
                    if response.status_code == 200:

                        cloudflare_api.objects.update_or_create(defaults={'user': user, 'global_api_key': api_key, 'email': email})
                        messages.success(request, 'updated Successfully Created')
                        return redirect('/admin/cf/hostname')
                    
                    else:
                        messages.warning(request, "'error': 'Failed to fetch data from Cloudflare API'")
                        return render(request, 'admin/cf_config.html', {'head': form_title, 'form': form})
            else:
                try:
                    query = cloudflare_api.objects.latest('id')
                    form = cf_api_key(instance=query)
                except:
                    form = cf_api_key()
                
            return render(request, 'admin/cf_config.html', {'head': form_title, 'form': form})
        
        else:
            return render(request, '404.html')
        
    
    else:
        return redirect('login')
    



def cf_main_domain(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            form_title = 'Cloudflare Authentigration'
            user = request.user
            try:
                query = cloudflare_api.objects.latest('id')

                if request.method == 'POST':
                    form = cf_hostname(request.POST)
                    if form.is_valid():
                        zone = form.cleaned_data['main_domain_name']
                        account_id = form.cleaned_data['account_id']
                        ip1 = form.cleaned_data['ip_address']
                        ip2 = form.cleaned_data['ip_address2']
                        # Make a request to the Cloudflare API
                        headers = {
                            'Content-Type': 'application/json',
                            'X-Auth-Email': query.email,
                            'X-Auth-Key': query.global_api_key
                        }
                        url = 'https://api.cloudflare.com/client/v4/zones'

                        # Data payload
                        data = {
                            "account": {
                                "id": account_id
                                },
                            "name": zone,
                            "type": "full"
                            }
                        
                        response = requests.post(url, headers=headers, json=data)
                        # Handle the response
                        if response.status_code == 200:
                            
                            zone_id = response.json()['result']['id']
                            dns_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
                            
                            dns_records = [
                                        {
                                            "type": "A",
                                            "name": "@",
                                            "content": ip1,  # Replace with your first IP address
                                            "ttl": 1,
                                            "proxied": True
                                        },
                                        {
                                            "type": "A",
                                            "name": "@",
                                            "content": ip2,  # Replace with your second IP address
                                            "ttl": 1,
                                            "proxied": True
                                        },
                                        {
                                            "type": "CNAME",
                                            "name": "*",  # Replace with your wildcard domain
                                            "content": zone,  # Replace with the target domain
                                            "ttl": 1,
                                            "proxied": True
                                        }
                                        ]
                            for record in dns_records:
                                dns_response = requests.post(dns_url, json=record, headers=headers)
                            if dns_response.status_code == 200:
                                cloudflare_api.objects.update_or_create(defaults={'user': user, 'main_domain_name': zone, 'account_id': account_id, 'ip_address':
                                                                                            ip1, 'ip_address2': ip2})
                                                                                             
                                
                                domains.objects.create(user=user, domain=zone, Description=zone, zone_id=zone_id)
                                
                                #get_id = domains.objects.get(user=user, domain=zone).id
                                messages.success(request, 'updated Successfully Created')
                                return redirect(f'/admin/cf/')
                        
                            else:
                                cloudflare_api.objects.update_or_create(defaults={'user': user, 'main_domain_name': zone, 'account_id': account_id, 'ip_address':
                                                                                            ip1, 'ip_address2': ip2})
                                try:
                                    
                                    domains.objects.create(user=user, domain=zone, Description=zone, zone_id=zone_id)
                                except:
                                    domains.objects.filter(user=user, domain=zone).update(zone_id=zone_id)

                                messages.success(request, 'updated Successfully Created')
                                return redirect(f'/admin/cf/')
                            
                        
                        else:
                            messages.warning(request, "'error': 'Failed to fetch data from Cloudflare API Account id or domain already exists'")
                            return render(request, 'admin/cf_config.html', {'head': form_title, 'form': form})

                else:
                    form = cf_hostname(instance=query)
                return render(request, 'admin/cf_config.html', {'head': form_title, 'form': form})
            
            except:
                return redirect('/admin/cf/')
        else:
            return render(request, '404.html')
    else:
        return redirect('login')
    

#     # Get the Cloudflare API key from settings
#     # api_key = 'h8r23OIoFACJIC-dHX38-WzxW46C9vdV8SUbYBrT'
#     account_id = '88d3c5e4f04d8b52b5031850dacc825c'  # Replace with your Cloudflare account ID
#     zone_name = 'technicalbikash.com'  # Replace with your domain name
#     # ip_address = '192.0.2.1'  # Replace with the IP address you want to point to
     
#     # Make a request to the Cloudflare API
#     headers = {
#         'Content-Type': 'application/json',
#         'X-Auth-Email': 'pokhrelb9@gmail.com',
#         'X-Auth-Key': 'dc0016264d8cee9d65defc28026be46650ccc'
#     }
#     url = 'https://api.cloudflare.com/client/v4/zones'

#     # Data payload
#     data = {
#         "account": {
#             "id": account_id
#         },
#         "name": zone_name,
#         "type": "full"
#     }

#     response = requests.post(url, headers=headers, json=data)
#    # Handle the response
#     if response.status_code == 200:
#         #data = response.json()
#         # Process the data as needed
#         return HttpResponse(response)
#     else:
#          return JsonResponse({'error': 'Failed to fetch data from Cloudflare API'}, status=500)



# def ff(request):
#     domains.objects.create(user=request.user, domain='test.com', Description='')


def ssl_origin(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            query = cloudflare_api.objects.latest('id')
            get_domain_query = domains.objects.get(domain=query.main_domain_name)
            get_zone_id = get_domain_query.zone_id
            
            doamin_name = get_domain_query.domain
            
            headers = {
                            'Content-Type': 'application/json',
                            'X-Auth-Email': query.email,
                            'X-Auth-Key': query.global_api_key
                        }
            url = f'https://api.cloudflare.com/client/v4/zones/{get_zone_id}/settings/ssl'
            

            data = {
                "value": "strict"
            }
            response = requests.patch(url, json=data, headers=headers)
            if response.status_code == 200:
                
                url_for_cert = f"https://api.cloudflare.com/client/v4/certificates"

                hostnames = [f"{doamin_name}", f"*.{doamin_name}"]
                csr_path = BASE_DIR / 'ssl/server.csr'
                # Read certificate and private key contents
                with open(csr_path, "r") as pem_file:
                    csr = pem_file.read()

                # data = {
                #         "certificate_request": csr,
                #         "hostnames": hostnames,
                #         "requested_validity": 5475  # Validity in days (15 years)
                #     }
                data = {
                        "csr": f"{csr}",
                        "hostnames": hostnames,
                        "request_type": "origin-rsa",
                        "requested_validity": 5475
                    }
                
                response2 = requests.post(url_for_cert, json=data, headers=headers)
                if response2.status_code == 200:
                    data = response2.json()
                    # Get the certificate value from the response JSON
                    certificate = data.get('result', {}).get('certificate')
                    # Save certificate to a PEM file
                    pem_filename = BASE_DIR / 'ssl/ssl-cert-snakeoil.pem'
                    with open(pem_filename, 'w') as pem_file:
                        pem_file.write(certificate)
                    messages.success(request, 'Certificate updated Successfully')
                    return redirect(f'/admin/cf/')
                
                else:
                    return JsonResponse({'error': 'Certificate not found in the response JSON.'}, status=400)
                
                #return redirect('/admin/cf/')
            else:
                return JsonResponse({'error': 'Failed to update SSL/TLS encryption mode.'}, status=500)

        else:
            return render(request, '404.html')
    else:
        return redirect('login')
