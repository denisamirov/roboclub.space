from django.contrib import admin
from .models import News, Type


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'news', 'created_at')
    list_display_links = ('title', 'type', 'news', 'created_at')
    search_fields = ('title', 'type', 'news', 'created_at')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Type, TypeAdmin)
