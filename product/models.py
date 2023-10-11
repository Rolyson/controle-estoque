from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categorys"

    name = models.CharField(max_length=255)


class Product(models.Model):
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"

    name           = models.CharField(max_length=255)
    cod_sku        = models.CharField(max_length=60, null=True, blank=True, unique=True)
    description    = models.TextField(null=True, blank=True)
    situation      = models.IntegerField(choices=[(1, "Active"), (2, "Inactive")], default=1)
    price_cost     = models.FloatField(null=True, blank=True)
    date_creation  = models.DateField(auto_now=True)
    category       = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


