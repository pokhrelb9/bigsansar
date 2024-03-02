from getpass import getpass

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from bigsansar.core.ubuntu import deploy


class Command(BaseCommand):
    help = "fully Setup server into ubuntu linux"

    def handle(self, *args, **options):
                print('configuring now')
                print('Bigsansar is available open-source under the MIT license. We recommend using the latest version of Python 3. Bigsansar is Fully based on django and linux ubuntu. You can use bigsansar for install packaged.')
                print('sure, Are you using Ubuntu lixu OS system')
                print("if your OS system is ubuntu then type 'Y' or 'y' else type any other ")
                get_input = input()
                if get_input == 'Y':
                    return deploy()
                
                elif get_input == 'y':
                    return deploy()
                
                else:
                    print('exit')
                    exit()
