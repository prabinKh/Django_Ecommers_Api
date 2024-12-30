from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'company_name', 'price', 'slug')
    prepopulated_fields = {'slug': ('company_name', 'product_name')}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "rating", "created_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_image", "category", "description", "price")