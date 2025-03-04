from django.contrib import admin
from .models import Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'parent', 'slug', 'created_at')
    list_filter = ('parent', 'created_at')
    search_fields = ('category_name', 'description')
    prepopulated_fields = {'slug': ('category_name',)}
    list_per_page = 20

    # 🔹 Show save button on top
    save_on_top = True
    
    
