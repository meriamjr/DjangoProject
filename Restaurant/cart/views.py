from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Products, Cart
from django.shortcuts import get_object_or_404, redirect
from django.core.serializers import serialize

def product_list(request):
    products = Products.objects.all()
    return render(request, 'browsing.html', {'products': products})

def view_cart(request):
    cart_items = Cart.objects.filter(status=False)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if product.qtestock > cart_item.quantity:
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart:view_cart')
    else:
        messages.error(request, "Stock insuffisant pour ajouter ce produit au panier.")
        return redirect('cart:view_cart')

def add_qty(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if product.qtestock > cart_item.quantity:
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart:view_cart')
    else:
        messages.error(request, "Stock insuffisant pour ajouter ce produit au panier.")
        return redirect('cart:view_cart')

def sub_qty(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('cart:view_cart')
    else:
        messages.warning(request, "La quantité ne peut pas être inférieure à 1.")
        return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
