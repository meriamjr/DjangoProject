from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Products, Cart
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Products.objects.all()
    return render(request, 'browsing.html', {'products': products})

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user,status=False)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    
    # Récupérer ou créer un élément du panier pour cet utilisateur et ce produit
    cart_item, created = Cart.objects.get_or_create(
    product=product,
    user=request.user,
    status=False # Panier en cours (non payé)
    )
    
    # Vérification du stock
    if product.qtestock > cart_item.quantity:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Produit ajouté au panier.")
    else:
        messages.error(request, "Stock insuffisant pour ajouter ce produit au panier.")
    return redirect('cart:view_cart')

@login_required
def add_qty(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item= Cart.objects.get_or_create(product=product,user=request.user,status=False).first()
    
    if cart_item:
        if product.qtestock > cart_item.quantity:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart:view_cart')
        else:
            messages.error(request, "Stock insuffisant pour ajouter ce produit au panier.")
    return redirect('cart:view_cart')

@login_required
def sub_qty(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product,user=request.user,
status=False).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return redirect('cart:view_cart')
        else:
            messages.warning(request, "La quantité ne peut pas être inférieure à 1.")
    else:
        messages.warning(request, "Le panier est vide.")
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
