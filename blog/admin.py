from django.contrib import admin
from .models import Post, Comment, Ad, SocialLink


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class AdAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "link")


admin.site.register(Ad, AdAdmin)


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    search_fields = ["name", "link"]


admin.site.register(SocialLink, SocialLinkAdmin)
