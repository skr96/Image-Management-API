from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
import getpass
from rest_framework.authtoken.models import Token
import os

class Command(BaseCommand):
    help = 'Get access key for user'

    def handle(self, *args, **options):
        username = raw_input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        try:
            # check if user already exists
            user = User.objects.get(username=username)
            self.stdout.write("User : " + username + " already exists.")
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # create folder for the user to store media
            media_path= os.path.join(os.getcwd(), 'IMAGES')
            os.makedirs(os.path.join(media_path, username))
            self.stdout.write("User " + username + " created.")

        token, created = Token.objects.get_or_create(user=user)
        self.stdout.write("Access key for " + username + " : ")
        print(token)

