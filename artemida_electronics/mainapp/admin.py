from django.contrib import admin
from .models import Processor, Motherboard, RAM, Cooler, Videocard

admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(Cooler)
admin.site.register(Videocard)
