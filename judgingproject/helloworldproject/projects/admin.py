
# Register your models here.
from django.contrib import admin
from .models import Client, Category, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'status', 'deadline', 'price')
    list_filter = ('status', 'category', 'deadline')
    search_fields = ('title', 'client__name') # クロス検索用インデックス

admin.site.register(Client)
admin.site.register(Category)