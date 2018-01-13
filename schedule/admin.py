from django.contrib import admin
from .models import Teacher,Course,Subject
# Register your models here.


admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Subject)

#class TeacherAdmin(Admin.ModelAdmin):
 #   list_display('first_name','last_name','email','salary')
  #  list_filter('first_name',)
   # search_field('first_name',)
    #pass



admin.site.site_header='BONJOUR'