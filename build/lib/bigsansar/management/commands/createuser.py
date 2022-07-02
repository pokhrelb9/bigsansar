from django.contrib.auth.models import User
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        print('We are creating 1000 fake user..............')


        print('please wait a minute.................')



        for _ in range(1000):
            try:

                get_uname = 'fake_'
                total_user = User.objects.last().id + 1
                username = get_uname + str(total_user)


            except:
                break

            else:

                create = User.objects.create_user(username=username, password='bp787898')

                print(create, '........ ok')


