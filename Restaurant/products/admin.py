from django.contrib import admin
from django.utils.html import format_html # Pour générer du HTML dans l'admin
from products.models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview','previewDescription',
    'detailDescription','price', 'qtestock', 'categorie') # Colonnes affichées dans la liste
    
    # Méthode pour afficher une prévisualisation de l'image
    def image_preview(self, obj):
        if obj.image: # Vérifie si une image est disponible
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.image)
        return "Pas d'image" # Message si aucune image n'est définie
    image_preview.short_description = "Image" # Intitulé de la colonne dans l'admin
    
    list_per_page = 10 # Nombre d'éléments affichés par page
    search_fields = ('title', 'previewDescription')
    list_filter = ('price', 'categorie')
    ordering = ('-qtestock', 'title')
    
#Enregistrement du modèle Products dans l'admin avec la configuration ProductsAdmin
admin.site.register(Products, ProductsAdmin)
