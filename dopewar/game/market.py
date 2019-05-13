from django.core.management.base import BaseCommand, CommandError
from dopewar5.dopewar.dopewar import settings
from django.conf import settings

import os, django
settings.configure(DEBUG=True)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dopewar5.dopewar.dopewar.settings'
django.setup()

from dopewar5.dopewar.game.models import country,drug

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    print(help)
    def handle(self, *args, **options):
        print('helloworld')
        USAcoke = drug.objects.get(id=1)
        USAcoke.price=12000
        USAcoke.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated'))
        print('completed')

