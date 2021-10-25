"""
All entities/models related to customer orders and their features
are contained here.

"""


from django.db import models

from store.models import Store, StoreItem


class OrderStatus(models.Model):
    """Status model for invoices. It contains all possible statuses for the
    invoices in the system"""

    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10, null=False)


class CustomerOrder(models.Model):
    """All customer orders are contained in this model, the store they
    were ordered from, their status and their items"""

    customer = models.ForeignKey("invoice.Customer", null=False, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, null=False, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, null=False, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    """Items contained in a customer order are contained in this model"""

    store_item = models.ForeignKey(StoreItem, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    customer_order = models.ForeignKey(CustomerOrder, null=False, on_delete=models.PROTECT)

