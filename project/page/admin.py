from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *

class PageAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ('tree_actions', 'indented_title', 'is_show', 'created', 'updated')
    list_display_links = ('indented_title',)

admin.site.register(Page, PageAdmin)
