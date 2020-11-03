from django.contrib import admin

# Register your models here.
from Dashboard.models import room, humidity, air_press, co2,temperature



admin.site.register(room)
admin.site.register(temperature)
admin.site.register(humidity)
admin.site.register(air_press)
admin.site.register(co2)
