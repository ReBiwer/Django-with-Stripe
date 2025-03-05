from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, db_index=True, verbose_name="Name")
    description = models.TextField(null=True, blank=True, db_index=True, verbose_name="Description")
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Price")
    currency = models.CharField(max_length=3, default='USD', choices=[
        ('usd', 'USD'),
        ('eur', 'EUR')
    ])

    def get_intent_url(self):
        return reverse('payment:get_intent', kwargs={'id': self.pk})


class Order(models.Model):
    items = models.ManyToManyField('Item')
    discount = models.ForeignKey('Discount', null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.ForeignKey('Tax', null=True, blank=True, on_delete=models.SET_NULL)

    def get_intent_url(self):
        return reverse('payment:get_intent', kwargs={'id': self.pk})

class Discount(models.Model):
    stripe_id = models.CharField(max_length=50)

class Tax(models.Model):
    stripe_id = models.CharField(max_length=50)