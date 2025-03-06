from django.contrib import admin
from django.utils.html import format_html # Pour générer du HTML dans l'admin
from categorie.models import Categorie

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('desCat', 'image_preview') # Utilisation d'une méthode personnalisée pour l'image
    # Méthode pour afficher une prévisualisation de l'image
    def image_preview(self, obj):
        if obj.imageCat: # Vérifie si une image est disponible
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.imageCat)
        
        return "Pas d'image" # Message si aucune image n'est définie
    
    image_preview.short_description = "Image" # Intitulé de la colonne dans l'admin
    
    # Enregistrement du modèle Categorie dans l'admin avec la configuration CategorieAdmin
admin.site.register(Categorie, CategorieAdmin)