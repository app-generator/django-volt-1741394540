# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    position = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Project(models.Model):

    #__Project_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    start date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Worker(models.Model):

    #__Worker_FIELDS__
    fte = models.IntegerField(null=True, blank=True)

    #__Worker_FIELDS__END

    class Meta:
        verbose_name        = _("Worker")
        verbose_name_plural = _("Worker")



#__MODELS__END
