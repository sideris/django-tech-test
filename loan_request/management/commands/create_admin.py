from django.core.management import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        User.objects.filter(email='admin@example.com').delete()
        User.objects.create_superuser('admin@example.com', 'admin', 'secret')