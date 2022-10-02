from django.contrib import admin
from .models import Processor, Motherboard, RAM, Cooler

admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(Cooler)
# Register your models here.
