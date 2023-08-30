import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Teacher

fakegen = Faker()

def populate(n=10):
    # print(n)
    for entry in range(n):
        fake_name = fakegen.name()
        subject_list = ['matemaatika', 'eesti keel', 'geograafia', 'kehaline kasvatus']
        print(f'{fake_name}, {subject_list}')
        Teacher.objects.get_or_create(name=fake_name, subject=random.choices(subject_list)[0])


populate() # create 5 person
# populate(20) # create 20 person
