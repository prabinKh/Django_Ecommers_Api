from django.contrib import admin
from .models import *

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "price", "stock", "created_at")
    prepopulated_fields = {"slug": ("name",)}  # Auto-generate slug from name
    fields = [
        "name",
        "brand",
        "description",
        "slug",  # Add slug explicitly here
        "processor",
        "ram",
        "storage",
        "gpu",
        "screen_size",
        "weight",
        "price",
        "discounted_price",
        "stock",
        "image1",
        "image2",
        "image3",
        "tags",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "rating", "created_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_image", "category", "description", "price")