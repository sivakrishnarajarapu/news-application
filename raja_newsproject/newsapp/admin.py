from django.contrib import admin
from newsapp.models import Student,Employee

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'marks']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr' ]

admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
