from django.core.management.base import BaseCommand
from Faker.script import manage_functions
class Command(BaseCommand):
    help = 'This comman creates fake data for User expression testing'  # Optional help text

    def handle(self, *args, **options):
        # Your script logic here
        manage_functions()
