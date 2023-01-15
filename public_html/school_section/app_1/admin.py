from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class SclassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class WaysAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'about', 'way', 'email', 'phone_number', 'date_registration')
    list_display_links = ('first_name', 'last_name', 'age', 'about', 'way', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'age', 'about', 'way', 'email', 'phone_number')

class QuestionAdmin(admin.ModelAdmin):
    list_display= ('q_1', 'name_text',)
    list_display_links= ('q_1', 'name_text',)


class GroupBookAdmin(admin.ModelAdmin):
    list_display= ('id_group',)

class SpeedTextAdmin(admin.ModelAdmin):
    list_display = ('name_text', 'id_group', 'text',)
    list_display_links = ('name_text', 'id_group',)
    search_fields = ('name_text', 'id_group', 'text',)




admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Ways, WaysAdmin)

admin.site.register(Group_text, GroupBookAdmin)
admin.site.register(SpeedText, SpeedTextAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(diary)
admin.site.register(Profile)


# admin.site.register(CustomUser)