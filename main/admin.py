from django.contrib import admin
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'title', 'content', 'post_added', 'author_id', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('post_added', 'title', 'author_id', 'is_published')
    list_editable = ('is_published',)

admin.site.register(Post, PostAdmin)
