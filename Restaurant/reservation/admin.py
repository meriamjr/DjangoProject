from django.contrib import admin

from reservation.models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nom_client','email' ,'date_reservation' ,
    'heure_reservation' , 'nombre_personnes' , 'commentaires' )
# Enregistrement du modèle Reservation dans l'admin avec la configuration ReservationAdmin
admin.site.register(Reservation, ReservationAdmin)