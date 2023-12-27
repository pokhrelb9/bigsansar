import os


def deploy():

    cmd1 = "sudo apt update  && sudo apt upgrade -y"
    os.system(cmd1)


    if os.path.isdir('www') == True:
        print('we are installing some ubuntu package for configurations....')
        cmd2 = "sudo apt install openssh-server ufw apache2 libapache2-mod-wsgi-py3 postgresql postgresql-contrib libpq-dev -y"
        os.system(cmd2)


    else:
        print("you have no any configurations file and folder . use 'bigsansar init' command line for internal configurations. then , type 'sudo bigsansar setup_server' again . ")
