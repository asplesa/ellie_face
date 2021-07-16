from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro',
        'article',
        'image',
        'date_added',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'article',
        'date_added',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
