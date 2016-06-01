from django.contrib import admin
from . import  models
from django.apps import apps
# Register your models here.
#admin.site.register(x for x in models)
#admin.site.register(for x in models.models)
    #[x for x in models])

#for model in apps.get_models():# (get_app('slaves')):
#    admin.site.register(model)

#admin.site.register(x for x in models)
admin.site.register([models.Master,models.Slave,models.Role])
#admin.site.register(models.Role)
#admin.site.register(models.Slave)