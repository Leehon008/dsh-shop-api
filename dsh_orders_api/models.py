#!/usr/bin/python 
from django.db import models
from django.urls import reverse


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Finished', 'Finished'),
    )
    
    revenue = models.CharField(max_length=200, db_index=True, verbose_name="revenue")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    quantity = models.PositiveIntegerField(verbose_name="stock")
    status = models.CharField(max_length=12, choices=ORDER_STATUS_CHOICES, verbose_name="status", default='Active')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')
    owner = models.ForeignKey('auth.User', related_name='order', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:OrderDetail', args=[self.id, self.slug])
