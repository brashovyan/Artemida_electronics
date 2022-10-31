from concurrent.futures import process
import email
from .models import Processor, Motherboard, RAM, Cooler, Videocard, Power_block, SSD_M2, HDD, SSD_sata, Corpus, Review
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
from cart.cart import Cart
from django.contrib.auth import authenticate, login, logout
from .forms import RegForm
from django.contrib.auth.models import User, Group


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
    try:
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

        if(processor_id != "" and cooler_id != "" and motherboard_id != "" and ram != "" and videocard_id != "" and power_block_id != "" and (hdd != "" or ssd_sata != "" or ssd_m2 != "")):
            cart = Cart(request)
            
            product = Processor.objects.get(id = int(processor_id))
            cart.add(product=product, quantity=1)

            product = Motherboard.objects.get(id = int(motherboard_id))
            cart.add(product=product, quantity=1)

            product = Cooler.objects.get(id = int(cooler_id))
            cart.add(product=product, quantity=1)

            product = Videocard.objects.get(id = int(videocard_id))
            cart.add(product=product, quantity=1)

            product = Power_block.objects.get(id = int(power_block_id))
            cart.add(product=product, quantity=1)

            if(corpus_id != ''):
                product = Corpus.objects.get(id = int(corpus_id))
                cart.add(product=product, quantity=1)

            ram = ram.split(',')
            for r in ram:
                r = r.split('%')
                product = RAM.objects.get(id = int(r[0]))
                cart.add(product=product, quantity=int(r[1]))

            if(ssd_m2 != ''):
                ssd_m2 = ssd_m2.split(',')
                for r in ssd_m2:
                    r = r.split('%')
                    product = SSD_M2.objects.get(id = int(r[0]))
                    cart.add(product=product, quantity=int(r[1]))

            if(hdd != ''):
                hdd = hdd.split(',')
                for r in hdd:
                    r = r.split('%')
                    product = HDD.objects.get(id = int(r[0]))
                    cart.add(product=product, quantity=int(r[1]))

            if(ssd_sata != ''):
                ssd_sata = ssd_sata.split(',')
                for r in ssd_sata:
                    r = r.split('%')
                    product = SSD_sata.objects.get(id = int(r[0]))
                    cart.add(product=product, quantity=int(r[1]))
            
            data = {
                "success": "success",
            }
            return JsonResponse(data)
        else:
            data = {
                "success": "fail",
            }
            return JsonResponse(data)
    except:
        return HttpResponseRedirect("/")


def info(request, product_id, product): # пожалуйста простите за этот ужас)
    if request.method == "POST":
        try:

            review_content = request.POST.get('review_content')

            processor = ''
            cooler = ''
            motherboard = ''
            ram = ''
            ssd_m2 = ''
            hdd = ''
            ssd_sata = ''
            videocard = ''
            power_block = ''
            corpus = ''

            if product == 'Processor':
                processor = Processor.objects.get(id = product_id)
                user = User.objects.get(id=request.user.id)
                review = Review.objects.create(creator = user, content = review_content) # создаю отзыв
                processor.review.add(review)
                return render(request, 'mainapp/info.html', {'processor': processor, 'cooler': cooler, 'motherboard':motherboard, 'ram':ram, 'ssd_m2':ssd_m2, 'hdd':hdd, 'ssd_sata':ssd_sata, 'videocard':videocard, 'power_block':power_block, 'corpus':corpus})

            elif product == 'Cooler':
                cooler = Cooler.objects.get(id = product_id)
            elif product == 'Motherboard':
                motherboard = Motherboard.objects.get(id = product_id)
            elif product == 'RAM':
                ram = RAM.objects.get(id = product_id)
            elif product == 'ssd_m2':
                ssd_m2 = SSD_M2.objects.get(id = product_id)
            elif product == 'HDD':
                hdd = HDD.objects.get(id = product_id)
            elif product == 'ssd_sata':
                ssd_sata = SSD_sata.objects.get(id = product_id)
            elif product == 'Videocard':
                videocard = Videocard.objects.get(id = product_id)
            elif product == 'Power_block':
                power_block = Power_block.objects.get(id = product_id)
            elif product == 'Corpus':
                corpus = Corpus.objects.get(id = product_id)
        except:
            return HttpResponseRedirect("/")

    else:
        try:
            processor = ''
            cooler = ''
            motherboard = ''
            ram = ''
            ssd_m2 = ''
            hdd = ''
            ssd_sata = ''
            videocard = ''
            power_block = ''
            corpus = ''

            if product == 'Processor':
                processor = Processor.objects.get(id = product_id)
            elif product == 'Cooler':
                cooler = Cooler.objects.get(id = product_id)
            elif product == 'Motherboard':
                motherboard = Motherboard.objects.get(id = product_id)
            elif product == 'RAM':
                ram = RAM.objects.get(id = product_id)
            elif product == 'ssd_m2':
                ssd_m2 = SSD_M2.objects.get(id = product_id)
            elif product == 'HDD':
                hdd = HDD.objects.get(id = product_id)
            elif product == 'ssd_sata':
                ssd_sata = SSD_sata.objects.get(id = product_id)
            elif product == 'Videocard':
                videocard = Videocard.objects.get(id = product_id)
            elif product == 'Power_block':
                power_block = Power_block.objects.get(id = product_id)
            elif product == 'Corpus':
                corpus = Corpus.objects.get(id = product_id)

            return render(request, 'mainapp/info.html', {'processor': processor, 'cooler': cooler, 'motherboard':motherboard, 'ram':ram, 'ssd_m2':ssd_m2, 'hdd':hdd, 'ssd_sata':ssd_sata, 'videocard':videocard, 'power_block':power_block, 'corpus':corpus})
        except:
            return HttpResponseRedirect("/")

def register(request): # регистрация
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                try:
                    em = User.objects.get(email = email) # проверяем уникальность почты
                    # если мы что то нашли и оказались тут, значит такая почта уже зарегана
                    error = "Данная почта уже использовалась для регистрации."
                    form = RegForm()
                    return render(request, 'mainapp/register.html', {'form': form, 'error': error})
                except:
                    # если почта свободна, то регаем дальше
                    try:
                        user = User.objects.create_user(username, email, password1)
                    except:
                        error = "Данный логин уже занят. Попробуйте другой."
                        form = RegForm()
                        return render(request, 'mainapp/register.html', {'form': form, 'error': error})                     

                if request.user.is_authenticated:
                    logout(request)
                login(request, user)

                return HttpResponseRedirect("/")
            else:
                error = "Пароли не совпадают!"
                form = RegForm()
                return render(request, 'mainapp/register.html', {'form': form, 'error':error})

        else:
            error = "Вы ввели некорректные данные! Повторите попытку, заполнив все поля по подсказкам."
            return render(request, 'mainapp/register.html', {'form': form, 'error': error})
    else:
        form = RegForm()
        return render(request, 'mainapp/register.html', {'form': form})


def logout1(request): #выход из учетной записи
    if request.user.is_authenticated:

        cart = Cart(request) # при выходе отчищаю корзину (с ней баги)
        cart.clear() # если этот код копируется в другой проект, то это можно удалить

        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def login1(request): #авторизация
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) # сначала пытаемся залогинить юзера по юзернейму
        if user is not None:
            login(request, user)

            cart = Cart(request) # при логине отчищаю корзину (с ней баги)
            cart.clear() # если этот код копируется в другой проект, то это можно удалить

            return HttpResponseRedirect("/")

            # если юзернейм правильный, но неправильный пароль, то дальше мы всё равно упремся в какую-то ошибку (не найдем почту)

        else: # если не получилось, то пытаемся по эмейлу
            try:
                u = User.objects.get(email=username)
                user = authenticate(request, username=u.username, password=password)
                if user is not None:
                    login(request, user)

                    cart = Cart(request)
                    cart.clear()

                    return HttpResponseRedirect("/")
                else: # если мы нашли эмейл, но неверный пароль
                    error = "Неверный логин или пароль! Проверьте раскладку языка. Также напоминаем, что буквы верхнего и нижнего регистра (строчные и заглавные) отличаются между собой."
                    return render(request, 'mainapp/login.html', {'error': error})
            except: # если мы не нашли эмейл
                error = "Неверный логин или пароль! Проверьте раскладку языка. Также напоминаем, что буквы верхнего и нижнего регистра (строчные и заглавные) отличаются между собой."
                return render(request, 'mainapp/login.html', {'error': error})
    else:
        if request.user.is_authenticated:
            logout(request)
        return render(request, 'mainapp/login.html')


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

