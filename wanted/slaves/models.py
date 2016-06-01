from django.conf import settings

from django.db import models

class Slave(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    s_fname = models.CharField(max_length=15)
    s_lname = models.CharField(max_length=15)
    s_descr = models.TextField()
    s_join_date = models.DateField(auto_now=True)
    cv = models.FileField(null=True,blank=True)


class Master(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    s_fname = models.CharField(max_length=15)
    s_lname = models.CharField(max_length=15)
    s_descr = models.TextField()
    s_join_date = models.DateField(auto_now=True)

class Role(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    #posted_by = models.CharField(max_length=15)
    posted_by = models.ForeignKey(Master)
    lname = models.CharField(max_length=15)
    r_descr = models.TextField()
    join_date = models.DateField(auto_now=True)


# Create your models here.
