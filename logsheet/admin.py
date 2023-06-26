from django.contrib import admin

# Register your models here.
from .models import DriverLogsheet


admin.site.register([DriverLogsheet,])
