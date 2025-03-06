from django.db import models
from categorie.models import Categorie

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=17)
    image = models.CharField(max_length=102)
    previewDescription = models.CharField(max_length=112)
    detailDescription = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    qtestock = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='products'