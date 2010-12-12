from django.db import models

class PaymentSource(models.Model):
    """
    A overriding payment source
    """
    order = models.ForeignKey('order.Order', related_name='alt-sources')
    source_type = models.CharField(max_length=128)
    initial_amount = models.IntegerField()
    balance = models.IntegerField()
    reference = models.CharField(max_length=128, blank=True, null=True)
