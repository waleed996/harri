"""
All entities/models related to invoices and their features
are contained here.

"""


from django.db import models
from order.models import CustomerOrder

from store.models import Store


class Customer(models.Model):
    """Customer model for all customers of the platform"""

    name = models.CharField(max_length=150, null=False)
    age = models.IntegerField()


class InvoiceStatus(models.Model):
    """Status model for invoices. It contains all possible statuses for the
    invoices in the system"""

    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10, null=False)


class Invoice(models.Model):
    """The Invoice model for Store sales, invoices for all stores
    are contained in this model and related through a foreign key
    relation with the Store model"""

    store = models.ForeignKey(Store, null=False, on_delete=models.CASCADE)
    status = models.ForeignKey(InvoiceStatus, null=False, on_delete=models.PROTECT)

    customer = models.ForeignKey(Customer, null=False, on_delete=models.PROTECT)

    customer_order = models.ForeignKey(CustomerOrder, null=False, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ("customer", "customer_order")