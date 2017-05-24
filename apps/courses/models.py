from __future__ import unicode_literals

from django.db import models


#
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=38)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
