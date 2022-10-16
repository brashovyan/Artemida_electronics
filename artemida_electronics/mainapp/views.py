from .models import Processor, Motherboard, RAM, Cooler, Videocard, Power_block, SSD_M2, HDD, SSD_sata, Corpus
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings


def index(request):
    processors = Processor.objects.all().order_by('price')
    motherboards = Motherboard.objects.all().order_by('price')
    rams = RAM.objects.all().order_by('price')
    coolers = Cooler.objects.all().order_by('price')
    videocards = Videocard.objects.all().order_by('price')
    power_blocks = Power_block.objects.all().order_by('price')
    ssd_m2 = SSD_M2.objects.all().order_by('price')
    hdd = HDD.objects.all().order_by('price')
    ssd_sata = SSD_sata.objects.all().order_by('price')
    corpuses = Corpus.objects.all().order_by('price')
    return render(request, 'mainapp/index.html', {'processors': processors, 'motherboards': motherboards, 'rams': rams, 'corpuses': corpuses,
     'coolers':coolers, 'videocards': videocards, 'power_blocks':power_blocks, 'ssd_m2': ssd_m2, 'hdd': hdd, 'ssd_sata':ssd_sata})
    


@receiver(post_delete, sender=Processor) # админ удалил процессор
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил процессор")
    except:
        print("Админ удалил процессор, но не удалось удалить картинку")


@receiver(post_delete, sender=Motherboard) # админ удалил мать
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил мать")
    except:
        print("Админ удалил мать, но не удалось удалить картинку")


@receiver(post_delete, sender=RAM) # админ удалил ОЗУ
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил ОЗУ")
    except:
        print("Админ удалил ОЗУ, но не удалось удалить картинку")


@receiver(post_delete, sender=Cooler) # админ удалил кулер
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил кулер")
    except:
        print("Админ удалил кулер, но не удалось удалить картинку")


@receiver(post_delete, sender=Videocard) # админ удалил видеокарту
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил видеокарту")
    except:
        print("Админ удалил видеокарту, но не удалось удалить картинку")


