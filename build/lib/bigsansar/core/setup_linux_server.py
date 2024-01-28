import os
import shutil
import site

from bigsansar.core.server_config_file import call_ssh

def init_setup():
        
        cmd = 'sudo django-admin startproject public_html /var/www/'
        print('creating a server .............')
        os.system(cmd)
        print('please wait...')

        get_content = "virtual_hosts = {" \
                      "\n   'localhost': 'public_html.urls'," \
                      "\n   'example.com': 'ex.urls'," \
                      "\n}"

        print('we are creating files...')
        f = open("/var/www/VirtualHost.py", "w")
        print(f)
        f.write(get_content)
        f.close()

        with open('/var/www/public_html/settings.py', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            count = 0
            f = open('/var/www/public_html/settings.py', 'w')

            for line in lines:
                # check if string present on a current line
                if line.find('INSTALLED_APPS') != -1:
                    count += 1
                    print('Installing Module in to INSTALLED_APPS')
                    x = lines.index(line) + count
                    print('Finding the Line Number:', x)
                    print('Inserting bigsansar module in to', line)

                    code = "    'bigsansar.apps.BigsansarConfig'," \
                           "\n" \
                           "    'bigsansar.contrib.account.apps.AccountConfig'," \
                           "\n" \
                           "    'bigsansar.contrib.sites.apps.SitesConfig'," \
                           "\n" \
                           "    'bigsansar.contrib.blogs.apps.BlogsConfig'," \
                           "\n" \
                           "    'ckeditor'," \
                           "\n" \
                           "    'ckeditor_uploader'," \
                           "\n" \
                           "    'bigsansar.contrib.advance.apps.AdvanceConfig'," \
                           "\n" \
                           "    'fontawesomefree'," \
                           "\n" \
                           "    'django.contrib.humanize'," \
                           "\n"

                    lines.insert(x, code)

                elif line.find('MIDDLEWARE = [') != -1:

                    print('Reading the lines MIDDLEWARE = [')
                    xy = lines.index(line) + 1
                    print('Finding the Line Number:', xy)
                    print('Inserting bigsansar virtualhost middleware  in to', line)

                    middlecode = "    'bigsansar.core.host.VirtualHostMiddleware'," \
                                 "\n"
                    lines.insert(xy, middlecode)

                elif line.find('ALLOWED_HOSTS = []') != -1:
                    xyz = lines.index(line)

                    # delete lines
                    del lines[xyz]

                    hostcode = "ALLOWED_HOSTS = ['*']" \
                               "\n" \
                               "\n" \
                               "# this is only for development mode" \
                               "\n" \
                               "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'" \
                               "\n" \
                               "\n" \
                               "ROOT_URLCONF = 'bigsansar.urls'" \
                               "\n" \
                               "\n" \
                               "#SECURE_SSL_REDIRECT = True" \
                               "\n" \
                               "MEDIA_ROOT = BASE_DIR/'media'" \
                               "\n" \
                               "MEDIA_URL = 'file/'" \
                               "\n" \
                               "CKEDITOR_UPLOAD_PATH = ''" \
                               "\n" \
                               "\n" \
                               "STATIC_ROOT = BASE_DIR/'static'" \
                               "\n" \
                               "\n" \
                               "SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')" \
                               "\n"

                    lines.insert(xyz, hostcode)

                elif line.find("ROOT_URLCONF = 'public_html.urls'") != -1:
                    rooturlindex = lines.index(line)

                    # delete lines
                    del lines[rooturlindex]

                elif line.find("'DIRS': [],") != -1:
                    getlinetemplate = lines.index(line)

                    # delete line for new setup
                    del lines[getlinetemplate]

                    newhomedirs = "        'DIRS': [BASE_DIR/'templates']," \
                                  "\n"

                    lines.insert(getlinetemplate, newhomedirs)

            contents = "".join(lines)
            f.write(contents)
            f.close()

        # Open a file with access mode 'a'
        with open("/var/www/public_html/urls.py", "w") as file_object:
            # Append 'hello' at the end of file
            file_object.write(''
                              'from django.conf import settings'
                              '\n'
                              'from django.conf.urls.static import static'
                              '\n'
                              'from django.contrib import admin'
                              '\n'
                              'from django.urls import include, path'
                              '\n'
                              '\n'
                              'urlpatterns = ['
                              '\n'
                              'path("filelist/", include("ckeditor_uploader.urls")),'
                              '\n'
                              'path("", admin.site.urls),'
                              '\n'
                              ']'
                              '\n'
                              '\n'
                              'urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'
                              '\n'
                              'admin.site.site_header = "BIGSANSAR"'
                              '\n'
                              'admin.site.site_title = "Bigsansar"'
                              '\n'
                              'admin.site.index_title = "bigsansar - create your own sites"'
                              '\n')
            # Close the file
            file_object.close()

        # Open a file with access mode 'a'
        with open("/var/www/public_html/settings.py", "a") as append_posgre:
            # Append 'postgres' at the end of file
            append_posgre.write(""
                              "# DATABASES = {"
                              "\n"
                              "#     'default': {"
                              "\n"
                              "#         'ENGINE': 'django.db.backends.postgresql',"
                              "\n"
                              "#         'NAME': 'database_name',"
                              "\n"
                              "#         'USER': 'username',"
                              "\n"
                              "#         'PASSWORD': 'password',"
                              "\n"
                              "#         'HOST': 'localhost',"
                              "\n"
                              "#         'PORT': '',"
                              "\n"
                              "#     }"
                              "\n"
                              "# }"
                              "\n"
                              "\n"
                              "CKEDITOR_CONFIGS = {"
                              "\n"
                              "'default': {"
                              "\n"
                              "'toolbar': 'full',"
                              "\n"
                              "'extraPlugins': ','.join("
                              "\n"
                              "['youtube','codesnippet']"
                              "\n"
                              "),}"
                              "\n"
                              "}"
                              "\n"
                              "\n"
                              "CKEDITOR_RESTRICT_BY_USER = True"
                              "\n"
                              "#CKEDITOR_ALLOW_NONIMAGE_FILES = False"
                              )
                              
            # Close the file
            append_posgre.close()

        with open("/var/www/public_html/wsgi.py", "w") as wsgifile:

            wsgifile.write('import os'
                           '\n'
                           'from django.core.wsgi import get_wsgi_application'
                           '\n'
                           '\n'
                           'os.environ["DJANGO_SETTINGS_MODULE"] = "public_html.settings"'
                           '\n'
                           'application = get_wsgi_application()'
                           '\n')

            wsgifile.close()

        cmd2 = 'sudo python3 /var/www/manage.py collectstatic'
        os.system(cmd2)

        with open('/var/www/public_html/settings.py', 'r') as static:
            # read all lines in a list
            rlines = static.readlines()
            count = 0
            sf = open('/var/www/public_html/settings.py', 'w')

            for line in rlines:
                # check if string present on a current line
                if line.find("STATIC_URL = 'static/'") != -1:
                    delurlstatic = rlines.index(line)

                    # delete lines
                    del rlines[delurlstatic]

                    staticdir = "STATIC_URL = 'files/'" \
                                "\n"

                    rlines.insert(delurlstatic, staticdir)

                elif line.find("STATIC_ROOT = BASE_DIR/'static'") != -1:
                    staticdirindex = rlines.index(line)

                    # delete lines
                    del rlines[staticdirindex]

                    chdirindex = "STATIC_DIR = BASE_DIR/'static'" \
                                 "\n" \
                                 "STATICFILES_DIRS = [STATIC_DIR, ]"

                    rlines.insert(staticdirindex, chdirindex)

            staticcontents = "".join(rlines)
            sf.write(staticcontents)
            sf.close()

        print('Finished')
    



def deploy_server():
    

    cmd1 = "sudo apt update  && sudo apt upgrade -y"
    os.system(cmd1)


    
    print('we are installing some ubuntu package for configurations....')
    cmd2 = "sudo apt install openssh-server ufw apache2 libapache2-mod-wsgi-py3 postgresql postgresql-contrib libpq-dev -y"
    os.system(cmd2)

    print(' RE-Configuring internal setiings now.................................................................')

    init_setup()
    

    print('secure on firewall...................................................')
    ufw = "sudo ufw allow OpenSSH && sudo ufw allow Apache && sudo ufw allow  'Apache Full' && sudo ufw allow 'Apache Secure' && sudo ufw allow 8000"
    os.system(ufw)

    print('configuration of apache2.....')
    chown_mod = 'sudo chown www-data /var/www && sudo chmod 775 /var/www'
    os.system(chown_mod)

    # for main setting of apache2
    lib_loc = site.getsitepackages()[0]
    
    # Construct the full path to the installed package directory
    
    big_loc = os.path.join(lib_loc, 'bigsansar')

    big_path = big_loc + '/etc/apache2.conf'
    shutil.copy(big_path, '/etc/apache2/apache2.conf')
    

    http_conf = big_loc + '/etc/000-default.conf'
    shutil.copy(http_conf, '/etc/apache2/sites-available/000-default.conf')

    #configuring in to 000-default.conf
    
    # postgresql setting here 

    #makemigration and migrate in to postgresql
    migrate = 'sudo python3 /var/www/manage.py makemigrations && sudo python3 /var/www/manage.py migrate' 
    os.system(migrate)
    
    # allow all module of server 
    package = "sudo a2ensite 000-default.conf && sudo a2enmod ssl && sudo a2ensite default-ssl.conf"
    os.system(package)

    site_packages = site.getsitepackages()[0]
    
    # Construct the full path to the installed package directory
    
    package_dir = os.path.join(site_packages, 'bigsansar')

    get_full_path = package_dir + '/etc/config_chroot.sh'
    # make
    print('restarting all service ...........................................')
    restart = "sudo %s && sudo sudo service apache2 restart && sudo ufw enable" % (get_full_path)
    os.system(restart)


    print('checking the service status........................................................ ')

    check = "sudo service ssh status && sudo service apache2 status && sudo service ufw status"
    os.system(check)
