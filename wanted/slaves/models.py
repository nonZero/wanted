from django.conf import settings

from django.db import models

class Slave(models.Model):
    # REVIEW: there is no need to add s_ in the front of each field. please remove.
    # REVIEW: Use descriptive names for fields (first_name, description)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    s_fname = models.CharField(max_length=15)
    s_lname = models.CharField(max_length=15)
    # REVIEW: should description allow null/blank values?
    s_descr = models.TextField()
    s_join_date = models.DateField(auto_now=True)
    # REVIEW: use upload_to to keep the files tidy in different folders
    cv = models.FileField(null=True,blank=True)


# REVIEW: better put all Master/Role models in a different app.
class Master(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    m_fname = models.CharField(max_length=15)
    m_lname = models.CharField(max_length=15)
    m_descr = models.TextField()
    m_join_date = models.DateField(auto_now=True)

class Role(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True)
    #posted_by = models.CharField(max_length=15)
    posted_by = models.ForeignKey(Master)
    lname = models.CharField(max_length=15)
    r_descr = models.TextField()
    join_date = models.DateField(auto_now=True)
