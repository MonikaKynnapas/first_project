import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Student

fakeGen = Faker()


def populate(n=5):
    # print(n)
    for entry in range(n):
        fake_name = fakeGen.name()
        fake_birth = fakeGen.date_between()
        fake_weight = random.randrange(50, 150)
        print(f'{fake_name}, {fake_birth}, {fake_weight}')
        # New Entry Student table
        Student.objects.get_or_create(name=fake_name, date_of_birth=fake_birth, weight=fake_weight)


populate()  # create 5 person
# populate(20) # create 20 person
