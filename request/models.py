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

    def save(self, *args, **kwargs):    

        status = {
                1 : 0, # Aberto
                2 : 0, # Atendido
                3 : 0, # Parcialmente
                4 : 0, # Corte
                5 : 0, # Cancelado
            }

        for item in self.productrequest_set.all():
            status[item.status] += 1

        if status[1] == 0 and status[2] == 0 and status[3] == 0 and status[4] == 0 and status[5] > 0:
            self.status = 5
        elif status[1] == 0 and status[3] == 0 and status[4] > 0:
            self.status = 4
        elif status[3] > 0:
            self.status = 3
        elif status[1] == 0 and status[3] == 0 and status[2] > 0:
            self.status = 2
        else:
            self.status = 1
        

        return super().save(*args, **kwargs)    

        
        super(Request, self).save(*args, **kwargs)  

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

    product         = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    sector          = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    type_movement   = models.IntegerField(choices=[(1, "In"), (2, "Out")])
    quantity        = models.FloatField()
    current         = models.FloatField(null=True, blank=True)
    previous        = models.FloatField(null=True, blank=True)
    request         = models.ForeignKey(Request, on_delete=models.DO_NOTHING)
    occurrence_data = models.DateTimeField(auto_now=True) 
    

    def save(self, *args, **kwargs):        

        current = 0

        # Obtem o estoque anterior
        previous_movemen = MovementProduct.objects.filter(sector=self.sector, product=self.product).last()
        if previous_movemen:
            current = previous_movemen.current

        if self.type_movement == 1: # se for entrada
            self.current = current + self.quantity
        else: # se for saída
            self.current = current - self.quantity

        self.previous = current
        super(MovementProduct, self).save(*args, **kwargs)  