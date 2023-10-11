from django.db import models

# Create your models here.
class Sector(models.Model):
    class Meta:
        verbose_name="Sector"
        verbose_name_plural="Sectors"

    name              = models.CharField(max_length=255)
    is_default_sector = models.BooleanField(default=False)