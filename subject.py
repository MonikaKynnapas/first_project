import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Subject

fakeGen = Faker()


def populate(n=10):

    for entry in range(n):
        subject_list = ['matemaatika', 'eesti keel', 'geograafia', 'kehaline kasvatus', 'majandus', 'turundus']
        print(f'{subject_list}')
        Subject.objects.get_or_create(name=random.choices(subject_list)[0])

populate()
