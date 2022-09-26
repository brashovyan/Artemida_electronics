from .models import Processor, Motherboard, RAM
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
    return render(request, 'mainapp/index.html', {'processors': processors, 'motherboards': motherboards, 'rams': rams})


@receiver(post_delete, sender=Processor) # админ удалил процессор
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил процессор")
    except:
        print("Админ удалил процессор, но не удалось удалить картинку")
