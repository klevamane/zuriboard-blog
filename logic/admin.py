from __future__ import absolute_import

from django.contrib import admin

from logic.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "title", "body", "created_at")
    list_display_links = ("id", "slug", "title", "body")
    ordering = ("created_at",)
    search_fields = ("title", "slug")
