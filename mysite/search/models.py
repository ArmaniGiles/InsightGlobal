from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Zipcode(models.Model):
  JURISDICTION_NAME = models.CharField(max_length=255)
  COUNT_FEMALE = models.CharField(max_length=255)
  COUNT_MALE = models.CharField(max_length=255)
  def __str__(self):
    return self.JURISDICTION_NAME
