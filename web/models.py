from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class SubCategories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Categories)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subcategory = models.ForeignKey(SubCategories)

    def __unicode__(self):
        return self.name
