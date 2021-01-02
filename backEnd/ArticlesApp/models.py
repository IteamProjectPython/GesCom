from django.db import models
#from decimal import Decimal
#from datetime import date

# Create your models here.

class Categories(models.Model):
    IdCategorie = models.AutoField(primary_key=True)
    Libelle = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    DateCreation = models.DateField()

class Articles(models.Model):
    IdArticle = models.AutoField(primary_key=True)
    Libelle = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    PrixUnitaire = models.DecimalField(("entrer un prix valide"), max_digits=10, decimal_places=2)
    DateCreation = models.DateField()
    IdCategorie = models.ForeignKey(Categories, on_delete=models.RESTRICT)