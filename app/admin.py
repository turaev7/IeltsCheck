from django.contrib import admin

from .models import *


class StudentAdmin(admin.ModelAdmin):    
    list_display=("familiya","ism","tel_raqam","tulov","one_id","rasm")
    list_filter = ['familiya', 'ism', 'tel_raqam',   'id']
    search_fields = ['familiya', 'ism', 'tel_raqam',   'id']
# admin.site.register(Payment)#,PayAdmin
# admin.site.register(Lesson)
admin.site.register(Student,StudentAdmin)
class IeltsAdmin(admin.ModelAdmin):
        list_display=("familiya","ism","tel_raqam","jinsi","ID","overal","img")
        list_filter = ['FIO']
        

admin.site.register(Full,IeltsAdmin)
class ReadingAdmin(admin.ModelAdmin):
        list_display=("familiya","ism","tel_raqam","jinsi","ID","overal","img")
        list_filter = ['FIO']
        
admin.site.register(Reading,ReadingAdmin)
class SpeakingAdmin(admin.ModelAdmin):
    list_display=("familiya","ism","tel_raqam","jinsi","ID","overal","img")
    list_filter = ['FIO']
    

admin.site.register(Speaking,SpeakingAdmin)
admin.site.register(Ielts_date)

