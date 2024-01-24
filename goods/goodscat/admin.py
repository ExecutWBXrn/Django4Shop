from django.contrib import admin
from .models import *

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "good", "price", "time_create", "is_published", "cat"]
    list_display_links = ["id", "good"]
    list_per_page = 5
    list_editable = "is_published",
    ordering = "time_update", "good"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]
    list_per_page = 5
    ordering = ["id"]