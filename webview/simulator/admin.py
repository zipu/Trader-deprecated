from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)


# Register your models here.
from simulator.models import FuturesInstrument

admin.site.register(FuturesInstrument)