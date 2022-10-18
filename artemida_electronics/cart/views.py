from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Processor
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse, HttpResponseRedirect


def cart_add(request, product_id):
    cart = Cart(request)
    product = Processor.objects.get(id = product_id)

    cart.add(product=product, quantity=1, update_quantity=False)

    return HttpResponseRedirect("/cart")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Processor, id=product_id)
    cart.remove(product)
    return redirect('/cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})