from django.contrib import admin
from .models import Processor, Motherboard, RAM

admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(RAM)
# Register your models here.
