
"""
from django.core.management.base import BaseCommand, CommandError
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
        SWIcoke = drug.objects.get(id=1)
        SWIcoke.price=12000
        USAcoke.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated'))
        print('completed')

"""

import random

def btc(past):
    if random.random() <= 0.8:
        coke = random.randint((round(int(past)*0.9)),(round(int(past)*1.1)))
        return round(coke, 0)
    else:
        options = ('up','down')
        selection = random.choice(options)
        if selection == 'up':
            coke = past*int(random.randrange(2,4))
            return round(coke, -1)
        if selection == 'down':
            coke = past/int(random.randrange(2,4))
            return round(coke, -1)

def USA_coke():
    if random.random() <= 0.8:
        coke = random.randint(4900,13000)
        return int(coke)
    else:
        coke = random.randint(3950,94500)
        return coke

def USA_mdma():
    if random.random() <= 0.8:
        mdma = random.randint(1200,2100)
        return mdma
    else:
        mdma = random.randint(987,16000)
        return mdma

def USA_lude():
    if random.random() <= 0.8:
        lude = random.randint(22,44)
        return lude
    else:
        lude = random.randint(11,55)
        return lude

def USA_hron():
    if random.random() <= 0.8:
        hron = random.randint(2899,3950)
        return hron
    else:
        hron = random.randint(1980,50000)
        return hron

def USA_meth():
    if random.random() <= 0.8:
        meth = random.randint(3899,4950)
        return meth
    else:
        meth = random.randint(2980,55000)
        return meth

def USA_acid():
    if random.random() <= 0.8:
        acid = random.randint(1800,3200)
        return acid
    else:
        acid = random.randint(1500,9000)
        return acid

def USA_pcp():
    if random.random() <= 0.8:
        acid = random.randint(400,800)
        return acid
    else:
        acid = random.randint(300,1200)
        return acid

def USA_hash():
    if random.random() <= 0.8:
        acid = random.randint(1800,3200)
        return acid
    else:
        acid = random.randint(1500,9000)
        return acid


def MEX_coke():
    if random.random() <= 0.8:
        coke = random.randint(4900,13000)
        return int(coke)
    else:
        coke = random.randint(3950,94500)
        return coke

def MEX_mdma():
    if random.random() <= 0.8:
        mdma = random.randint(1200,2100)
        return mdma
    else:
        mdma = random.randint(987,16000)
        return mdma

def MEX_lude():
    if random.random() <= 0.8:
        lude = random.randint(22,44)
        return lude
    else:
        lude = random.randint(11,55)
        return lude

def MEX_hron():
    if random.random() <= 0.8:
        hron = random.randint(2899,3950)
        return hron
    else:
        hron = random.randint(1980,50000)
        return hron

def MEX_meth():
    if random.random() <= 0.8:
        meth = random.randint(3899,4950)
        return meth
    else:
        meth = random.randint(2980,55000)
        return meth

def MEX_acid():
    if random.random() <= 0.8:
        acid = random.randint(1800,3200)
        return acid
    else:
        acid = random.randint(1500,9000)
        return acid

def MEX_pcp():
    if random.random() <= 0.8:
        acid = random.randint(400,800)
        return acid
    else:
        acid = random.randint(300,1200)
        return acid

def MEX_hash():
    if random.random() <= 0.8:
        acid = random.randint(1800,3200)
        return acid
    else:
        acid = random.randint(1500,9000)
        return acid


def SWISS_coke():
    if random.random() <= 0.8:
        coke = random.randint(4900,13000)
        return int(coke)
    else:
        coke = random.randint(3950,94500)
        return coke

def SWISS_mdma():
    if random.random() <= 0.8:
        mdma = random.randint(1200,2100)
        return mdma
    else:
        mdma = random.randint(987,16000)
        return mdma

def SWISS_lude():
    if random.random() <= 0.8:
        lude = random.randint(22,44)
        return lude
    else:
        lude = random.randint(11,55)
        return lude

def SWISS_hron():
    if random.random() <= 0.8:
        hron = random.randint(2899,3950)
        return hron
    else:
        hron = random.randint(1980,50000)
        return hron

def SWISS_meth():
    if random.random() <= 0.8:
        meth = random.randint(3899,4950)
        return meth
    else:
        meth = random.randint(2980,55000)
        return meth

def SWISS_acid():
    if random.random() <= 0.8:
        acid = random.randint(1800,3200)
        return acid
    else:
        acid = random.randint(1500,9000)
        return acid

def SWISS_pcp():
    if random.random() <= 0.8:
        acid = random.randint(400,800)
        return acid
    else:
        acid = random.randint(300,1200)
        return acid

def SWISS_hash():
    if random.random() <= 0.8:
        acid = random.randint(1800,3200)
        return acid
    else:
        acid = random.randint(1500,9000)
        return acid

