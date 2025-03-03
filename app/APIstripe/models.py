from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, db_index=True, verbose_name="Name")
    description = models.TextField(null=True, blank=True, db_index=True, verbose_name="Description")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Price")
