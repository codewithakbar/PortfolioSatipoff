from django.contrib import admin
from .models import PostPortfolio, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(PostPortfolio)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'publish')