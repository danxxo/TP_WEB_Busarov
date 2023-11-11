from django.core.management import BaseCommand, CommandParser
from django.contrib.auth.models import User

from app.models import User, Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            if user.username == 'admin':
                continue
            user.delete()
        for tag in Tag.objects.all():
            tag.delete()
        


