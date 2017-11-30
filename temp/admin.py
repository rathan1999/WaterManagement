from __future__ import unicode_literals
from django.contrib import admin
from .models import Sensors
from .models import Plant
from .models import waterBody
from .models import weatherStation
# Register your models here.
admin.site.register(Sensors)
admin.site.register(Plant)
admin.site.register(waterBody)
admin.site.register(weatherStation)