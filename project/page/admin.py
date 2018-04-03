from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug')

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'is_show', 'created', 'updated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
