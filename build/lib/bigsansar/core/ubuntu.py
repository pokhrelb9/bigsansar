import os
import shutil
import subprocess


get_pyversion = subprocess.check_output('sudo python3 -V', shell=True).decode('utf-8').strip()
pyversion = get_pyversion.rsplit('.', 1)[0].replace("P", "p").replace(" ","")

def deploy():

    cmd1 = "sudo apt update  && sudo apt upgrade -y"
    os.system(cmd1)


    
    print('we are installing some ubuntu package for configurations....')
    cmd2 = "sudo apt install openssh-server ufw apache2 libapache2-mod-wsgi-py3 postgresql postgresql-contrib libpq-dev -y"
    os.system(cmd2)

    print(' RE-Configuring internal setiings now.................................................................')

    # setting for apache cgi
    
    file_to_copy = '/usr/local/lib/%s/dist-packages/bigsansar/etc/serve-cgi-bin.conf' % (pyversion)
    destination_directory = '/etc/apache2/conf-available/'
    shutil.copy(file_to_copy, destination_directory)

    # copy cgi-bin main file 
    cgi_main_file = '/usr/local/lib/%s/dist-packages/bigsansar/main.py' % (pyversion)
    to_cgi_bin = '/usr/lib/cgi-bin/'
    shutil.copy(cgi_main_file, to_cgi_bin)
    to_cgi_bin_chmod = to_cgi_bin + '/main.py'
    os.chmod(to_cgi_bin_chmod, 0o755)

    # configuring sshd file 
    ssh_file = '/usr/local/lib/%s/dist-packages/bigsansar/etc/sshd_config' % (pyversion)
    ssh_to = '/etc/ssh/'
    shutil.copy(ssh_file,ssh_to) 

    # make a chroot environment
    # Open the file in append mode and use 'with' to ensure proper file closure
    with open('/etc/ssh/sshd_config', 'a') as file:
        # Use subprocess.run for better security and handling of command execution
        sudo_user = subprocess.run(['whoami'], stdout=subprocess.PIPE, text=True).stdout.strip()

        # Format the chroot_text
        chroot_text = f"Match User *,!{sudo_user}\nChrootDirectory %h\n"

        # Write the formatted text to the file
        file.write(chroot_text)

    # global settings of apache2
    apache2_conf = '/usr/local/lib/%s/dist-packages/bigsansar/etc/apache2.conf' % (pyversion)
    apache2_to = '/etc/apache2/'
    shutil.copy(apache2_conf, apache2_to)



    print('secure on firewall...................................................')
    ufw = "sudo ufw allow OpenSSH && sudo ufw allow Apache && sudo ufw allow  'Apache Full' && sudo ufw allow 'Apache Secure'"
    os.system(ufw)


    # allow all module of server 
    package = "sudo a2enmod cgi && sudo a2ensite 000-default.conf && sudo a2enmod ssl && sudo a2ensite default-ssl.conf && sudo a2enmod rewrite"
    os.system(package)

    print('restarting all service ...........................................')
    restart = "sudo service ssh restart && sudo service apache2 restart && sudo ufw enable"
    os.system(restart)

    print('checking the service status........................................................ ')

    check = "sudo service ssh status && sudo service apache2 status && sudo service ufw status"
    os.system(check)
