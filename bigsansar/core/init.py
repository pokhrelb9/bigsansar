import os
import subprocess

def initsetup():

    cmd = 'django-admin startproject www .'
    createfile = 'VirtualHost.py'
    get_content = 'virtual_hosts = {"test.com:8000": "root.urls", "example.com:8000": "ex.urls", }'
    print('please wait...')

    print('we are creating files...')
    f = open(createfile, "w")
    print(f)
    f.write(get_content)
    f.close()
    print('creating a server .............')
    os.system(cmd)
    print('cuccessfully created ...')
    print('finished...')
