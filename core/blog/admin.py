from django.contrib import admin
from .models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title',)

admin.site.register(Category)