from django.contrib import admin, messages
from .models import *

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "good", "price", "time_create", "is_published", "cat", "brief_info"]
    list_display_links = ["id", "good"]
    list_per_page = 5
    list_editable = ["is_published"]
    ordering = ["time_update", "good"]
    actions = ["set_published", "set_draft"]

    @admin.display(description="further information", ordering="describe")
    def brief_info(self, good: Goods):
        return f"symbols in description: {len(good.describe)}"
    @admin.action(description="published")
    def set_published(self, request, queryset):
        self.message_user(request, f"Кількість оновленних постів: {queryset.update(is_published=Goods.STATUS.PUBLISHED)}")

    @admin.action(description="draft")
    def set_draft(self, requset, queryset):
        self.message_user(requset, f"{queryset.update(is_published=Goods.STATUS.DRAFT)} постів знято з публікації", messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]
    list_per_page = 5
    ordering = ["id"]