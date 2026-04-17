from getpass import getpass

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create multiple user at once time "

    def handle(self, *args, **options):
        print('We are creating User..............')

        print('please wait a minute.................')

        print('How many user you want to create?')
        numbers = int(input())

        print('wait..........')
        print(''
              '')

        print('Put your password here')
        password = getpass()

        for _ in range(numbers):
            try:

                get_uname = 'user'
                total_user = User.objects.last().id + 1
                username = get_uname + str(total_user)

            except:
                break

            else:

                create = User.objects.create_user(username=username, password=password)

                print(create, '........ ok')

            finally:
                print('User created successfully')
                print('Finished')

