""" Admin for the product app """

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from image_cropping import ImageCroppingMixin

from . import models

__author__ = 'Shamima Akter Shampa, Aupourbau Koumar'
__copyright__ = 'Copyright 2017, Maison Mahdil'


# Inlines
class ProductImageInline(ImageCroppingMixin, SortableInlineAdminMixin, admin.TabularInline):
    model = models.ProductImage
    extra = 0
    fields = (
        'id',
        'image',
        'image_cropping',
        'title',
    )

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
                obj.updated_by = request.user
        obj.save()

class ProductVariantInline(ImageCroppingMixin, admin.StackedInline):
    model = models.ProductVariant
    exclude = ['slug']
    extra = 0

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
                obj.updated_by = request.user
        obj.save()

# Admins
@admin.register(models.Category)
class CategoryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'active',
                'name',
                'description',
                'image',
                'image_cropping',
            )
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'id',
                'created_by',
                'created_on',
                'updated_by',
                'updated_on',
            ),
        }),
    )
    list_display = (
        'name',
        'description',
        'updated_on',
        'updated_by',
    )
    readonly_fields = (
        'id',
        'created_by',
        'created_on',
        'updated_by',
        'updated_on',
    )

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
                obj.updated_by = request.user
        obj.save()


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'active',
                'name',
                'title',
                'description',
                'description2',
                'background_image',
                'background_image_cropping',
                'category',
                'related_product',
            )
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'id',
                'created_by',
                'created_on',
                'updated_by',
                'updated_on',
            ),
        }),
    )
    inlines = [
        ProductImageInline,
        ProductVariantInline,
    ]
    list_display = (
        'name',
        'image_tag',
        'title',
        'updated_on',
        'updated_by',
    )
    list_display_links = (
        'name',
        'image_tag',
    )
    list_filter = (
        'active',
        'category',
    )
    readonly_fields = (
        'id',
        'created_by',
        'created_on',
        'updated_by',
        'updated_on',
    )

    def save_model(self, request, obj, form, change):
        if change:
            if request.user:
                obj.updated_by = request.user
        else:
            if request.user:
                obj.created_by = request.user
                obj.updated_by = request.user
        obj.save()
