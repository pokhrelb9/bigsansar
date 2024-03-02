
import os
import site
from bigsansar.core.pip_package import copy_file_from_pip_lib
from www.settings import BASE_DIR


def deploy():

    print('RE-Configuring now')
    print('removing related file and folider')
    os.system('sudo rm -v /etc/ssh/sshd_config')
    source_ssh = copy_file_from_pip_lib('etc/sshd_config')
    os.system('sudo cp -v %s /etc/ssh/' % (source_ssh))
    print('Configuring internal setiings now.................................................................')

    file_path = "www/settings.py"
        # Text to be deleted
    text_to_delete = '''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
        # Read the content of the file
    with open(file_path, 'r') as file:
            content = file.read()

        # Remove the specified text
    modified_content = content.replace(text_to_delete, '')

        # Write the modified content back to the file
    with open(file_path, 'w') as file:
            file.write(modified_content)

    print("Text removed successfully.")

    os.system('sudo apt update  && sudo apt upgrade -y')

    print('we are installing some ubuntu package for configurations....')
    os.system('sudo apt install openssh-server ufw apache2 libapache2-mod-wsgi-py3 postgresql postgresql-contrib libpq-dev -y')

    print('secure on firewall...................................................')
    os.system("sudo ufw allow OpenSSH && sudo ufw allow Apache && sudo ufw allow  'Apache Full' && sudo ufw allow 'Apache Secure' && sudo ufw allow 8000")

    print('configuration of apache2.....')

    if not os.path.exists('ssl'):
                os.makedirs('ssl')
                
    else:
         print('already exit............')

    ssl_cert_snakeoil = 'ssl/ssl-cert-snakeoil.key'
    ssl_cert_pem = 'ssl/ssl-cert-snakeoil.pem'
    full_url_for_cert_key = os.path.join(BASE_DIR, ssl_cert_snakeoil)
    get_pem_cert_url = os.path.join(BASE_DIR, ssl_cert_pem)
    os.system('sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout %s -out %s' % (full_url_for_cert_key, get_pem_cert_url))
    os.system('sudo chown -R www-data %s && sudo chmod -R 775 %s' % (BASE_DIR, BASE_DIR))

    # for main setting of apache2
    lib_loc = site.getsitepackages()[0]
    
    # Construct the full path to the installed package directory
    
    big_loc = os.path.join(lib_loc, 'bigsansar')

    big_path = big_loc + '/etc/apache2.conf'
    os.system('sudo cp -v %s /etc/apache2/apache2.conf' % (big_path))

    venv_loc = os.environ['VIRTUAL_ENV']


    conf_before = """

<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin report@bigsansar.com
        #DocumentRoot /var/www/html

        Alias /files %s/static
        <Directory %s/static>
                require all granted
        </Directory>

        Alias /file %s/media
        <Directory %s/media>
                require all granted
        </Directory>

        <Directory %s/www>
        <files wsgi.py>
                require all granted
        </files>
        </Directory>

        WSGIDaemonProcess bigsansar.com restart-interval=30 graceful-timeout=10 python-path=%s python-home=%s
        WSGIProcessGroup bigsansar.com
        WSGIScriptAlias / %s/www/wsgi.py

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
""" % (BASE_DIR, BASE_DIR, BASE_DIR, BASE_DIR, BASE_DIR, BASE_DIR, venv_loc, BASE_DIR)


    file_http = open('000-default.conf', 'w')
    file_http.write(conf_before)
    file_http.close()

    #configuring in to 000-default.conf
    http_conf = os.path.join(BASE_DIR, '000-default.conf')
    os.system('sudo mv -v %s /etc/apache2/sites-available/' % (http_conf))

    # for ssl 
    venv_loc_ssl = os.environ['VIRTUAL_ENV']
    ssl_conf = """

<IfModule mod_ssl.c>
        <VirtualHost _default_:443>
                ServerAdmin report@bigsansar.com

                #DocumentRoot /var/www/html

                Alias /files %s/static
                <Directory %s/static>
                        require all granted
                </Directory>

                Alias /file %s/media
                <Directory %s/media>
                        require all granted
                </Directory>

                <Directory %s/www>
                <files wsgi.py>
                        require all granted
                </files>
                </Directory>

                WSGIDaemonProcess bigsansar.com_ssl restart-interval=30 graceful-timeout=10 python-path=%s python-home=%s
                WSGIProcessGroup bigsansar.com_ssl
                WSGIScriptAlias / %s/www/wsgi.py


                # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
                # error, crit, alert, emerg.
                # It is also possible to configure the loglevel for particular
                # modules, e.g.
                #LogLevel info ssl:warn

                ErrorLog ${APACHE_LOG_DIR}/error.log
                CustomLog ${APACHE_LOG_DIR}/access.log combined

                # For most configuration files from conf-available/, which are
                # enabled or disabled at a global level, it is possible to
                # include a line for only one particular virtual host. For example the
                # following line enables the CGI configuration for this host only
                # after it has been globally disabled with "a2disconf".
                #Include conf-available/serve-cgi-bin.conf

                #   SSL Engine Switch:
                #   Enable/Disable SSL for this virtual host.
                SSLEngine on

                #   A self-signed (snakeoil) certificate can be created by installing
                #   the ssl-cert package. See
                #   /usr/share/doc/apache2/README.Debian.gz for more info.
                #   If both key and certificate are stored in the same file, only the
                #   SSLCertificateFile directive is needed.
                SSLCertificateFile %s/ssl/ssl-cert-snakeoil.pem
                SSLCertificateKeyFile %s/ssl/ssl-cert-snakeoil.key

                #   Server Certificate Chain:
                #   Point SSLCertificateChainFile at a file containing the
                #   concatenation of PEM encoded CA certificates which form the
                #   certificate chain for the server certificate. Alternatively
                #   the referenced file can be the same as SSLCertificateFile
                #   when the CA certificates are directly appended to the server
                #   certificate for convinience.
                #SSLCertificateChainFile /etc/apache2/ssl.crt/server-ca.crt

                #   Certificate Authority (CA):
                #   Set the CA certificate verification path where to find CA
                #   certificates for client authentication or alternatively one
                #   huge file containing all of them (file must be PEM encoded)
                #   Note: Inside SSLCACertificatePath you need hash symlinks
                #                to point to the certificate files. Use the provided
                #                Makefile to update the hash symlinks after changes.
                #SSLCACertificatePath /etc/ssl/certs/
                #SSLCACertificateFile /etc/apache2/ssl.crt/ca-bundle.crt

                #   Certificate Revocation Lists (CRL):
                #   Set the CA revocation path where to find CA CRLs for client
                #   authentication or alternatively one huge file containing all
                #   of them (file must be PEM encoded)
                #   Note: Inside SSLCARevocationPath you need hash symlinks
                #                to point to the certificate files. Use the provided
                #                Makefile to update the hash symlinks after changes.
                #SSLCARevocationPath /etc/apache2/ssl.crl/
                #SSLCARevocationFile /etc/apache2/ssl.crl/ca-bundle.crl

                #   Client Authentication (Type):
                #   Client certificate verification type and depth.  Types are
                #   none, optional, require and optional_no_ca.  Depth is a
                #   number which specifies how deeply to verify the certificate
                #   issuer chain before deciding the certificate is not valid.
                #SSLVerifyClient require
                #SSLVerifyDepth  10

                #   SSL Engine Options:
                #   Set various options for the SSL engine.
                #   o FakeBasicAuth:
                #        Translate the client X.509 into a Basic Authorisation.  This means that
                #        the standard Auth/DBMAuth methods can be used for access control.  The
                #        user name is the `one line' version of the client's X.509 certificate.
                #        Note that no password is obtained from the user. Every entry in the user
                #        file needs this password: `xxj31ZMTZzkVA'.
                #   o ExportCertData:
                #        This exports two additional environment variables: SSL_CLIENT_CERT and
                #        SSL_SERVER_CERT. These contain the PEM-encoded certificates of the
                #        server (always existing) and the client (only existing when client
                #        authentication is used). This can be used to import the certificates
                #        into CGI scripts.
                #   o StdEnvVars:
                #        This exports the standard SSL/TLS related `SSL_*' environment variables.
                #        Per default this exportation is switched off for performance reasons,
                #        because the extraction step is an expensive operation and is usually
                #        useless for serving static content. So one usually enables the
                #        exportation for CGI and SSI requests only.
                #   o OptRenegotiate:
                #        This enables optimized SSL connection renegotiation handling when SSL
                #        directives are used in per-directory context.
                #SSLOptions +FakeBasicAuth +ExportCertData +StrictRequire
                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                                SSLOptions +StdEnvVars
                </Directory>

                #   SSL Protocol Adjustments:
                #   The safe and default but still SSL/TLS standard compliant shutdown
                #   approach is that mod_ssl sends the close notify alert but doesn't wait for
                #   the close notify alert from client. When you need a different shutdown
                #   approach you can use one of the following variables:
                #   o ssl-unclean-shutdown:
                #        This forces an unclean shutdown when the connection is closed, i.e. no
                #        SSL close notify alert is send or allowed to received.  This violates
                #        the SSL/TLS standard but is needed for some brain-dead browsers. Use
                #        this when you receive I/O errors because of the standard approach where
                #        mod_ssl sends the close notify alert.
                #   o ssl-accurate-shutdown:
                #        This forces an accurate shutdown when the connection is closed, i.e. a
                #        SSL close notify alert is send and mod_ssl waits for the close notify
                #        alert of the client. This is 100 percent SSL/TLS standard compliant, but in
                #        practice often causes hanging connections with brain-dead browsers. Use
                #        this only for browsers where you know that their SSL implementation
                #        works correctly.
                #   Notice: Most problems of broken clients are also related to the HTTP
                #   keep-alive facility, so you usually additionally want to disable
                #   keep-alive for those clients, too. Use variable "nokeepalive" for this.
                #   Similarly, one has to force some clients to use HTTP/1.0 to workaround
                #   their broken HTTP/1.1 implementation. Use variables "downgrade-1.0" and
                #   "force-response-1.0" for this.
                # BrowserMatch "MSIE [2-6]" \
                #               nokeepalive ssl-unclean-shutdown \
                #               downgrade-1.0 force-response-1.0

        </VirtualHost>
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
""" % (BASE_DIR, BASE_DIR, BASE_DIR, BASE_DIR, BASE_DIR, BASE_DIR, venv_loc_ssl, BASE_DIR, BASE_DIR, BASE_DIR)
    
    file_https = open('default-ssl.conf', 'w')
    file_https.write(ssl_conf)
    file_https.close()

    #configuring in to 000-default.conf
    https_conf = os.path.join(BASE_DIR, 'default-ssl.conf')
    os.system('sudo mv -v %s /etc/apache2/sites-available/' % (https_conf))

    # postgresql setting here 
    psycopy2 = 'pip install psycopg2'
    os.system(psycopy2)

    # for main setting of postgres
    postgres_loc = site.getsitepackages()[0]
    big_loc_db = os.path.join(postgres_loc, 'bigsansar')

    cmd_db = 'python %s/etc/db.py' % (big_loc_db)
    os.system(cmd_db)

    #makemigration and migrate in to postgresql
    migrate = 'python manage.py makemigrations && python manage.py migrate' 
    os.system(migrate)

    print('creating superuser for access to the admin pannel ...............................')
    os.system('python manage.py createsuperuser')
    # allow all module of server 
    package = "sudo a2ensite 000-default.conf && sudo a2enmod ssl && sudo a2ensite default-ssl.conf && sudo a2enmod wsgi"
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

    check = "sudo service ssh status && sudo service ufw status && sudo service apache2 status"
    os.system(check)
    

    

    
