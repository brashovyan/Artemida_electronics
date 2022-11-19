from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Processor, Motherboard, Cooler, RAM, HDD, SSD_M2, SSD_sata, Videocard, Power_block, Corpus, Review, History
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group


def cart_add(request, product_id, product):
    cart = Cart(request)
    
    if('Processor' in str(product)):
        pr = Processor.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('Cooler' in str(product)):
        pr = Cooler.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('Motherboard' in str(product)):
        pr = Motherboard.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('RAM' in str(product)):
        pr = RAM.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('HDD' in str(product)):
        pr = HDD.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('SSD_M2' in str(product)):
        pr = SSD_M2.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('SSD_sata' in str(product)):
        pr = SSD_sata.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('Videocard' in str(product)):
        pr = Videocard.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('Power_block' in str(product)):
        pr = Power_block.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    elif('Corpus' in str(product)):
        pr = Corpus.objects.get(id=product_id)
        cart.add(pr, quantity=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id, product):

    cart = Cart(request)
    # Да, костыльно и топорно, но честно я пытался сделать по нормальному)

    if('Processor' in str(product)):
        pr = Processor.objects.get(id=product_id)
        cart.remove(pr)

    elif('Cooler' in str(product)):
        pr = Cooler.objects.get(id=product_id)
        cart.remove(pr)

    elif('Motherboard' in str(product)):
        pr = Motherboard.objects.get(id=product_id)
        cart.remove(pr)

    elif('RAM' in str(product)):
        pr = RAM.objects.get(id=product_id)
        cart.remove(pr)

    elif('HDD' in str(product)):
        pr = HDD.objects.get(id=product_id)
        cart.remove(pr)

    elif('SSD_M2' in str(product)):
        pr = SSD_M2.objects.get(id=product_id)
        cart.remove(pr)

    elif('SSD_sata' in str(product)):
        pr = SSD_sata.objects.get(id=product_id)
        cart.remove(pr)

    elif('Videocard' in str(product)):
        pr = Videocard.objects.get(id=product_id)
        cart.remove(pr)

    elif('Power_block' in str(product)):
        pr = Power_block.objects.get(id=product_id)
        cart.remove(pr)

    elif('Corpus' in str(product)):
        pr = Corpus.objects.get(id=product_id)
        cart.remove(pr)

    return HttpResponseRedirect("/cart")


def cart_info(request, product_id, product):

    if('Processor' in str(product)):
        pr = Processor.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/Processor")

    elif('Cooler' in str(product)):
        pr = Cooler.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/Cooler")

    elif('Motherboard' in str(product)):
        pr = Motherboard.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/Motherboard")

    elif('RAM' in str(product)):
        pr = RAM.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/RAM")

    elif('HDD' in str(product)):
        pr = HDD.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/HDD")

    elif('SSD_M2' in str(product)):
        pr = SSD_M2.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/SSD_M2")

    elif('SSD_sata' in str(product)):
        pr = SSD_sata.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/SSD_sata")

    elif('Videocard' in str(product)):
        pr = Videocard.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/Videocard")

    elif('Power_block' in str(product)):
        pr = Power_block.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/Power_block")

    elif('Corpus' in str(product)):
        pr = Corpus.objects.get(id=product_id)
        return HttpResponseRedirect(f"/info/{pr.id}/Corpus")

    return HttpResponseRedirect("/cart")


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def change_quantity_plus(request, product_id, product):
    cart = Cart(request)
    # Да, костыльно и топорно, но честно я пытался сделать по нормальному)
    # (или лень)

    if('Processor' in str(product)):
        pr = Processor.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('Cooler' in str(product)):
        pr = Cooler.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('Motherboard' in str(product)):
        pr = Motherboard.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('RAM' in str(product)):
        pr = RAM.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('HDD' in str(product)):
        pr = HDD.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('SSD_M2' in str(product)):
        pr = SSD_M2.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('SSD_sata' in str(product)):
        pr = SSD_sata.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('Videocard' in str(product)):
        pr = Videocard.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('Power_block' in str(product)):
        pr = Power_block.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    elif('Corpus' in str(product)):
        pr = Corpus.objects.get(id=product_id)
        cart.add(pr, update_quantity='Plus')

    return HttpResponseRedirect("/cart")


def change_quantity_minus(request, product_id, product):
    cart = Cart(request)
    # Да, костыльно и топорно, но честно я пытался сделать по нормальному)
    # (или лень)

    if('Processor' in str(product)):
        pr = Processor.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('Cooler' in str(product)):
        pr = Cooler.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('Motherboard' in str(product)):
        pr = Motherboard.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('RAM' in str(product)):
        pr = RAM.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('HDD' in str(product)):
        pr = HDD.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('SSD_M2' in str(product)):
        pr = SSD_M2.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('SSD_sata' in str(product)):
        pr = SSD_sata.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('Videocard' in str(product)):
        pr = Videocard.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('Power_block' in str(product)):
        pr = Power_block.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')

    elif('Corpus' in str(product)):
        pr = Corpus.objects.get(id=product_id)
        cart.add(pr, update_quantity='Minus')
    return HttpResponseRedirect("/cart")


def clear(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponseRedirect("/cart")


def success(request):
    cart = Cart(request)
    
    if cart.len() == 0:
        return HttpResponse('Корзина пуста')

    receipt = 'Ваш чек:\n'
    for item in cart: # сначала проверяем всё ли ок, есть ли такие товары в наличии
        if (item['product'].stock - item['quantity']) < 0:
            return HttpResponse('Во время оплаты заказа произошла ошибка! Возможно, какой-то товар отсутствует на складе. Попробуйте обновить страницу и повторить попытку.')

    s = 0
    for item in cart: # если всё ок, то сохраняем изменение кол-ва товара, проводим оплату и пишем чек
        s += item['price']
        item['product'].stock -= item['quantity']
        item['product'].save()
        receipt += f"{item['product'].title} - {item['quantity']} шт => {item['price']*item['quantity']} руб.\n"
    receipt += f"Итого: {s} рублей"    
        
    if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            History.objects.create(buyer = user, content=receipt)

    cart.clear()
    return render(request, 'cart/success.html')