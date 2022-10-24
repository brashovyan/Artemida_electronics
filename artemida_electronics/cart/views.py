from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Processor, Motherboard, Cooler, RAM, HDD, SSD_M2, SSD_sata, Videocard, Power_block, Corpus
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse, HttpResponseRedirect


def cart_add(request, product_id):
    """cart = Cart(request)
    product = Motherboard.objects.get(id = 3)
    cart.add(product=product, quantity=1, update_quantity=False)"""

    return HttpResponseRedirect("/cart")


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


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})