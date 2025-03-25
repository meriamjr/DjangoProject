from django.http import JsonResponse
from django.conf import settings
from django.http.response import JsonResponse
import stripe
from django.shortcuts import render,redirect
from cart.models import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    # Récupérer les items du panier à partir de la fonction utilitaire
    cart_items = get_cart_items(request)    # Préparer les items pour Stripe
    line_items = []
    for item in cart_items:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item['product']['title'],
                },
                'unit_amount': int(item['product']['price'] * 100),  # En centimes
            },
            'quantity': item['quantity'],
        })
    # Créer une session de paiement Stripe
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://localhost:8000/payments/success/",
            cancel_url="http://localhost:8000/payments/cancel/",
        )
        return JsonResponse({"id": session.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@login_required
def get_cart_items(request):
    # récupérer les articles du modèle Cart
    cart_items = []  # Déplacez l'initialisation ici pour l'assurer en dehors de la boucle
    cart_objects = Cart.objects.select_related('product').filter(user=request.user,
status=False)
    
    for cart in cart_objects:
        cart_items.append({
            "product": {
                "title": cart.product.title,
                "price": cart.product.price,
            },
            "quantity": cart.quantity,
        })
    return cart_items

def success(request):
    # Appeler la fonction pour mettre à jour les articles du panier
    process_payment(request)
    return render(request, "success.html")

def cancel(request):
    return render(request, "cancel.html")

def process_payment(request):
# Supposons que le paiement a été validé
    payment_successful = True # Remplacez par la logique de votre paiement réel
    
    if payment_successful:
    # Mettre à jour le status des éléments du panier à True (payé)
        cart_items = Cart.objects.all()
    
        for item in cart_items:
            item.status = True # Mettre à jour le status à True
            item.save()
        
        messages.success(request, "Paiement effectué avec succès !")
        return redirect('cart:view_cart')
    else:
        messages.error(request, "Le paiement a échoué. Veuillez réessayer.")
        return redirect('cart:view_cart')