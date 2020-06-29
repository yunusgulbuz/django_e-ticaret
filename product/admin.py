from django.contrib import admin
from .models import (
    Category,
    Product,
    Images,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'image_tag',
    ]
    list_display_links = [
        'title',
        'status',
    ]


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryProduct(admin.ModelAdmin):
    list_display = [
        'title',
        'status',
        'image_tag',
        'create_at',
    ]
    list_display_links = [
        'title',
    ]
    list_filter = [
        'price',
        'status',
    ]
    inlines = [
        ProductImageInline,
    ]


class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'product',
        'image_tag',
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, CategoryProduct)
admin.site.register(Images, ImageAdmin)
