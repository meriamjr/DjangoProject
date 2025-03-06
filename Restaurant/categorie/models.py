from django.db import models

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    desCat = models.CharField(max_length=30)
    imageCat = models.CharField(max_length=250)
    
    def __str__(self):
        return self.desCat