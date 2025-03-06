from django.shortcuts import render
from categorie.models import Categorie
from products.models import Products

def index(request):
    categories = Categorie.objects.all() # Récupère toutes les catégories
    products = Products.objects.all() # Récupère tous les produits
    return render(request, 'index.html', {'categories': categories, 'products':
    products})