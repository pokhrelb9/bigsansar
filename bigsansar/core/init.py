import os
import shutil




def initsetup():

    if os.path.isdir('www') == True:

        print('RE-Configuring now')
        print('removing related file and folider')
        os.remove('manage.py')
        shutil.rmtree('www')
        print('re installing internal package')
        return config()

    else:
        return config()

def config():
        
        cmd = 'django-admin startproject www .'
        print('creating a server .............')
        os.system(cmd)
        print('please wait...')

        get_content = "virtual_hosts = {" \
                      "\n   'example1.com': 'www.urls'," \
                      "\n   'example.com': 'ex.urls'," \
                      "\n}"

        print('we are creating files...')
        f = open("VirtualHost.py", "w")
        print(f)
        f.write(get_content)
        f.close()

        with open('www/settings.py', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            count = 0
            f = open('www/settings.py', 'w')

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

                elif line.find("ROOT_URLCONF = 'www.urls'") != -1:
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
        with open("www/urls.py", "w") as file_object:
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
        with open("www/settings.py", "a") as append_posgre:
            # Append 'postgres' at the end of file
            append_posgre.write(""
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

        with open("www/wsgi.py", "w") as wsgifile:

            wsgifile.write('import os'
                           '\n'
                           'from django.core.wsgi import get_wsgi_application'
                           '\n'
                           '\n'
                           'os.environ["DJANGO_SETTINGS_MODULE"] = "www.settings"'
                           '\n'
                           'application = get_wsgi_application()'
                           '\n')

            wsgifile.close()

        cmd1 = 'python manage.py migrate'
        cmd2 = 'python manage.py collectstatic'

        os.system(cmd1)
        os.system(cmd2)

        with open('www/settings.py', 'r') as static:
            # read all lines in a list
            rlines = static.readlines()
            count = 0
            sf = open('www/settings.py', 'w')

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