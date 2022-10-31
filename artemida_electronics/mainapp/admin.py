from django.contrib import admin
from .models import Processor, Motherboard, RAM, Cooler, Videocard, Power_block, SSD_M2, HDD, SSD_sata, Corpus, Review

admin.site.register(Processor)
admin.site.register(HDD)
admin.site.register(SSD_sata)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(Cooler)
admin.site.register(Videocard)
admin.site.register(Power_block)
admin.site.register(SSD_M2)
admin.site.register(Corpus)
admin.site.register(Review)
