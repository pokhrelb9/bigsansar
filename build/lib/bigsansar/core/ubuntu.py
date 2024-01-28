
import os
import shutil
from bigsansar.core.pip_package import copy_file_from_pip_lib

from bigsansar.core.setup_linux_server import deploy_server


def deploy():
    if os.path.isdir('/var/www/public_html') == True:

        print('RE-Configuring now')
        print('removing related file and folider')
        os.remove('/var/www/manage.py')
        shutil.rmtree('/var/www/public_html')
        os.remove('/etc/ssh/sshd_config')
        ssh_file = 'etc/sshd_config'
        to = '/etc/ssh'
        copy_file_from_pip_lib(ssh_file, to)

        print('re installing internal package')
        return deploy_server()
        
    
    else:
        return deploy_server()
    


