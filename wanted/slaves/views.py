from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView

import datetime

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Sum
from django.shortcuts import redirect
from django.utils.encoding import escape_uri_path
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from . import forms
from . import models



def ShowSl(req):
    return render(req,"main_sl.html")


class ListSlavesView(ListView):
    page_title = "Slaves"
    model = models.Slave

    #def get_queryset(self):
    #    return super().get_queryset().filter(account__user=self.request.user)

    def get_queryset(self):
        return super().get_queryset() #.filter(account__user=self.request.user) .aggregate(sum=Sum('amount'))['sum']
