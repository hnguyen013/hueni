from django.contrib import admin

from .models import TeamMember, SiteContent


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role')
    ordering = ('order',)


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('key', 'section', 'title', 'order')
    list_filter = ('section',)
    list_editable = ('order',)
    search_fields = ('key', 'title', 'body')
    prepopulated_fields = {'key': ('title',)}
    ordering = ('section', 'order')
