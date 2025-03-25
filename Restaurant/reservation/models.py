from django.db import models

class Reservation(models.Model):
    nom_client = models.CharField(max_length=100)
    email = models.EmailField()
    date_reservation = models.DateField()
    heure_reservation = models.TimeField()
    nombre_personnes = models.IntegerField()
    commentaires = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nom_client} - {self.date_reservation} à {self.heure_reservation}"