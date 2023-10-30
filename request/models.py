from itertools import product
from django.db import models
from product.models import Product
from sector.models import Sector

# Create your models here.
class Request(models.Model):
    class Meta:
        verbose_name="Request"
        verbose_name_plural="Requests"

    description = models.CharField(max_length=255)
    sector_in   = models.ForeignKey(Sector, on_delete=models.DO_NOTHING, related_name="sector_in")
    sector_out  = models.ForeignKey(Sector, on_delete=models.DO_NOTHING, related_name="sector_out")
    status      = models.IntegerField(default=1)
    # status = [
    #     (1, "Aberto"), 
    #     (2, "Atendido"), 
    #     (3, "Atendido parcialmente"), 
    #     (4, "Atendido com corte"), 
    #     (5, "Cancelado"), 
    # ]

class ProductRequest(models.Model):
    class Meta:
        verbose_name="Product Request"
        verbose_name_plural="Products Requests"

    request         = models.ForeignKey(Request, on_delete=models.DO_NOTHING)
    product         = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity        = models.FloatField()
    quantity_served = models.FloatField(default=0)
    is_consumable   = models.BooleanField(default=False)
    status          = models.IntegerField(default=1)
    # status = [
    #     (1, "Aberto"), 
    #     (2, "Atendido"), 
    #     (3, "Atendido parcialmente"), 
    #     (4, "Atendido com corte"), 
    #     (5, "Cancelado"), 
    # ]

class MovementProduct(models.Model):
    class Meta:
        verbose_name="Movement Product"
        verbose_name_plural="Movements Products"

    product       = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    sector        = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    type_movement = models.IntegerField(choices=[(1, "In"), (2, "Out")])
    quantity      = models.FloatField()
    current       = models.FloatField(null=True, blank=True)
    previous      = models.FloatField(null=True, blank=True)
    request       = models.ForeignKey(Request, on_delete=models.DO_NOTHING)
    