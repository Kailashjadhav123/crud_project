from django.contrib import admin
from .models import Student

# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'age', 'city', 'mobile')

admin.site.register(Student, Studentadmin)