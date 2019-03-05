from django.contrib import admin
from .models import Publisher,Author,Book,Teacher,Course,Subject,Student,Patient,Doctor,Person,Laptop,Construction,Buildings
# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','salary')
    list_filter=('first_name',)
    search_field=('first_name',)
    #pass

admin.site.register(Teacher,TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','location','email','image','file')
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Student,StudentAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','city','country')
admin.site.register(Publisher,PublisherAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('aname','email')
admin.site.register(Author,AuthorAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','course_duration','fee')
admin.site.register(Course,CourseAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher')
admin.site.register(Book,BookAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display=('name','aadhar','mobile','address','bhamashah')
    list_filter=('aadhar',)
    search_field=('name')
admin.site.register(Patient,PatientAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('Dname','Ddepartment','Dage','Dfee','Dprofile','Demail','Dhospital')
    list_filter = ('Ddepartment',)
    search_fields = ('Dname',)
admin.site.register(Doctor,DoctorAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('fname','lname')
    list_filter = ('fname',)
admin.site.register(Person,PersonAdmin)

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('per','icolor')
    list_filter = ('per',)
admin.site.register(Laptop,LaptopAdmin)

class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('fname','lname')
    list_filter = ('fname',)
admin.site.register(Construction,ConstructionAdmin)

class BuildingsAdmin(admin.ModelAdmin):
    list_display =('construction','area')
admin.site.register(Buildings,BuildingsAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','fee','course','teacher')
admin.site.register(Subject,SubjectAdmin)



admin.site.site_header='BONJOUR'