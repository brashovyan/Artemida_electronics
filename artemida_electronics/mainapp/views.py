from .models import Processor, Motherboard, RAM, Cooler, Videocard, Power_block, SSD_M2, HDD, SSD_sata, Corpus
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
    

def aja(request):
    processor_id = request.GET.get('processor')
    cooler_id = request.GET.get('cooler')
    motherboard_id = request.GET.get('motherboard')
    ram = request.GET.get('ram')
    ssd_m2 = request.GET.get('ssd_m2')
    hdd = request.GET.get('hdd')
    ssd_sata = request.GET.get('ssd_sata')
    videocard_id = request.GET.get('videocard')
    power_block_id = request.GET.get('power_block')
    corpus_id = request.GET.get('corpus')

    print(f'processor {processor_id}')
    """print(f'cooler {cooler}')
    print(f'mother {motherboard}')
    print(f'ram {ram}')
    print(f'ssd_m2 {ssd_m2}')
    print(f'hdd {hdd}')
    print(f'ssd_sata {ssd_sata}')
    print(f'videocard {videocard}')
    print(f'powerblock {power_block}')
    print(f'corpus {corpus}')"""

    processor = Processor.objects.get(id=processor_id)


    if(processor_id != "" and cooler_id != "" and motherboard_id != "" and ram != "" and videocard_id != "" and power_block_id != "" and (hdd != "" or ssd_sata != "" or ssd_m2 != "")):
        data = {
            "success": "success",
        }
        return JsonResponse(data)
    else:
        data = {
            "success": "fail",
        }
        return JsonResponse(data)


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


@receiver(post_delete, sender=Power_block) # админ удалил бп
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил блок питания")
    except:
        print("Админ удалил блок питания, но не удалось удалить картинку")


@receiver(post_delete, sender=SSD_M2) # админ удалил ssd m2
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил ссд м2")
    except:
        print("Админ удалил ссд м2, но не удалось удалить картинку")


@receiver(post_delete, sender=HDD) # админ удалил жесткий диск
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил жесткий диск")
    except:
        print("Админ удалил жесткий диск, но не удалось удалить картинку")


@receiver(post_delete, sender=SSD_sata) # админ удалил ссд сата
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил ссд сата")
    except:
        print("Админ удалил ссд сата, но не удалось удалить картинку")


@receiver(post_delete, sender=Corpus) # админ удалил корпус
def delete_article(sender, instance, **kwargs):
    try:
        os.remove(r"./media/"+str(instance.image))
        print("Админ удалил корпус")
    except:
        print("Админ удалил корпус, но не удалось удалить картинку")

