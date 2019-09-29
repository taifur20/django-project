""" Models for the product app """

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer
from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping.fields import ImageRatioField, ImageCropField

from django.db import models

__author__ = 'Sathi'
__copyright__ = 'Copyright 2019'


# Functions
def variant_file_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (slugify(instance.slug), ext)
    return "product/%s/%s" % (
        timezone.now().strftime('%Y/%m/%d'),
        filename)


# Models
class Category(models.Model):

    # Attributes
    active = models.BooleanField(
        _('active'),
        default=False
    )
    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _('image'),
        blank=True,
        null=True,
        upload_to='product/category/%Y/%m/%d',
        help_text=_("For optimal quality, we recommend that you choose images that are at least 1600px wide"),
    )
    image_cropping = ImageRatioField(
        'image',
        '1600x900'
    )
    name = models.CharField(
        _('name'),
        max_length=120,
        unique=True,
    )
    slug = models.SlugField(
        _('slug'),
        editable=False,
        unique=True,
    )

    # Meta Data
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('created by'),
    )
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('updated by'),
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['name']
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    # Functions
    def __str__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return u"%s" % (self.name)

    def get_absolute_url(self):
        return reverse('', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super(Category, self).save()
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Product(models.Model):

    # Relations
    category = models.ManyToManyField(
        'Category',
        blank=True,
        verbose_name=_('categories'),
    )
    related_product = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name=_('related products'),
    )

    # Attributes
    active = models.BooleanField(
        _('active'),
        default=False
    )
    description = RichTextUploadingField(
        _('description'),
        blank=True,
        null=True,
    )
    description2 = models.TextField(
        _('description2'),
        blank=True,
        null=True,
    )
    background_image = models.ImageField(
        _('background_image'),
        upload_to='product/%Y/%m/%d',
        help_text=_("For optimal quality, we recommend that you choose images that are at least 1600px wide"),
    )
    background_image_cropping = ImageRatioField(
        'background_image',
        '1600x900'
    )
    name = models.CharField(
        _('name'),
        max_length=120,
        unique=True,
    )
    slug = models.SlugField(
        _('slug'),
        editable=False,
        unique=True,
    )
    title = models.CharField(
        _('title'),
        blank=True,
        max_length=120,
        null=True,
    )

    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('created by'),
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('updated by'),
    )

    # Meta
    class Meta:
        ordering = ['name']
        verbose_name = _('product')
        verbose_name_plural = _('products')

    # Functions
    def __str__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return u"%s" % (self.name)

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'slug': self.slug})

    def background_image_cropping_url(self):
        if self.background_image:
            return get_thumbnailer(self.background_image).get_thumbnail({
                'size': (1600, 900),
                'box': self.background_image_cropping,
                'crop': True,
                'detail': True,
            }).url

    def image_tag(self):
        _('image'),
        if self.background_image:
            return mark_safe('<img src="%s" height="100" />' % (self.background_image.url))
        else:
            return "%s" % (_('None'))

    def save(self, *args, **kwargs):
        super(Product, self).save()
        self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):

    # Relations
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name=_('product'),
    )

    # Attributes
    image = models.ImageField(
        _('image'),
        upload_to='product/product/%Y/%m/%d',
        help_text=_("For optimal quality, we recommend that you choose images that are at least 1600px wide"),
    )
    image_cropping = ImageRatioField(
        'image',
        '1600x900'
    )
    position = models.PositiveIntegerField(
        blank=False,
        default=0,
        null=False
    )
    title = models.CharField(
        _('title'),
        blank=True,
        max_length=120,
        null=True,
    )

    # Meta Data
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('created by'),
    )
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name=_('updated by'),
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['position']
        verbose_name = _('product image')
        verbose_name_plural = _('product images')

    # Functions
    def __str__(self):
        return "%s - %s" % (self.product.name, self.id)

    def __unicode__(self):
        return u"%s - %s" % (self.product.name, self.id)

    def image_cropping_url(self):
        if self.image:
            return get_thumbnailer(self.image).get_thumbnail({
                'size': (1600, 900),
                'box': self.image_cropping,
                'crop': True,
                'detail': True,
            }).url

    def save(self, *args, **kwargs):
        super(ProductImage, self).save(*args, **kwargs)
        if self.position == 0:
            self.position = self.id
        return super(ProductImage, self).save(*args, **kwargs)


class ProductVariant(models.Model):

    # Relations
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        verbose_name=_('product'),
    )

    # Attributes
    cost_price = models.DecimalField(
        _('cost price'),
        decimal_places=2,
        max_digits=8,
        default=0,
    )
    description = models.TextField(
        _('description'),
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _('image'),
        blank=True,
        null=True,
        upload_to=variant_file_upload_to,
    )
    image_cropping = ImageRatioField(
        'image',
        '1600x1600'
    )
    name = models.CharField(
        _('name'),
        max_length=120,
        unique=True,
    )
    sale_price = models.DecimalField(
        _('sale price'),
        decimal_places=2,
        default=0,
        max_digits=8,
    )
    slug = models.SlugField(
        _('slug'),
        unique=True,
        max_length=206,
    )
    vat = models.DecimalField(
        _('VAT %'),
        decimal_places=2,
        default=0,
        max_digits=5,
    )

    # Meta Data
    created_on = models.DateTimeField(
        _('created on'),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_on = models.DateTimeField(
        _('updated on'),
        auto_now=True,
        editable=False,
        null=True,
    )

    # Meta
    class Meta:
        ordering = ['name']
        verbose_name = _('product variant')
        verbose_name_plural = _('products variant')

    # Functions
    def __str__(self):
        return "%s - %s" % (self.product.name, self.name)

    def __unicode__(self):
        return u"%s - %s" % (self.product.name, self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(ProductVariant, self).save(*args, **kwargs)
