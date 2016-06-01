from django.shortcuts import render

# Create your views here.

def ShowSl(req):
    return render(req,"main_sl.html")