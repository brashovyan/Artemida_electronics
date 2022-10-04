from .models import Processor, Motherboard, RAM, Cooler, Videocard
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
import random


def index(request):
    processors = Processor.objects.all()
    motherboards = Motherboard.objects.all()
    rams = RAM.objects.all()
    coolers = Cooler.objects.all()
    videocards = Videocard.objects.all()
    return render(request, 'mainapp/index.html', {'processors': processors, 'motherboards': motherboards, 'rams': rams, 'coolers':coolers, 'videocards': videocards})


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


