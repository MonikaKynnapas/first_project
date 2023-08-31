from django.db import models
from django.contrib import admin

# Create your models here.
class Student(models.Model):
    """ Student database table """
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    weight = models.IntegerField()

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['weight']

    def birthday(self, obj):
        """ Stackoverflow 7216764 23086383 Change date format on admin page"""
        if obj.date_of_birth is not None:
            return obj.date_of_birth.strftime('%d.%m.%Y')

    list_display = ['name', 'birthday', 'weight']
    list_per_page = 10

class Teacher(models.Model):
    """ Teacher database table """
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)

    # def __str__(self):
        # return f'{self.name} õpetab {self.subject}'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    list_per_page = 10

class Subject(models.Model):
    subject = models.CharField(max_length=100)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']