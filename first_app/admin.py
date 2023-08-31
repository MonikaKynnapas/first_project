from django.contrib import admin
from .models import Student, StudentAdmin
from .models import Teacher, TeacherAdmin
from .models import Subject, SubjectAdmin

# Register your models here.
# Show in admin page
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)

