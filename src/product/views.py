""" Views for the product app """

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from . import models

__author__ = 'Sathi'
__copyright__ = 'Copyright 2019'


# Views
def product_list(request):
    product_list = models.Product.objects.all()
    context = {
        'product_list': product_list,
        'navbar': 'product',
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug=None):
    instance_product = get_object_or_404(models.Product, slug=slug)
    product_list = models.Product.objects.exclude(slug=slug)
    context = {
        'instance_product': instance_product,
        'product_list': product_list,
        'navbar': 'product',
    }
    return render(request, 'products/product_detail.html', context)
