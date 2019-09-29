# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

__author__ = 'Sathi'
__copyright__ = 'Copyright 2019, Maison Mahdil'


# Models
class Contact(models.Model):

    # Attributes
    name = models.CharField(
        _('name'),
        max_length=120,
    )
    subject = models.CharField(
        _('subject'),
        max_length=120,
    )
    description = models.TextField(
        _('description'),
    )
    email = models.EmailField(
        _('Email'),
    )
    phone = models.CharField(
        _('phone number'),
        max_length=120,
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
        ordering = ['-created_on']
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    # Functions
    def __str__(self):
        return self.name
