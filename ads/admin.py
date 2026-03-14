from django.contrib import admin
from .models import Category, Advertisement, Resume

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'author', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description', 'location']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['profession', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['profession', 'skills']
