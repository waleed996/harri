"""
All entities/models related to store and their features
are contained here.

"""


from django.db import models


class StoreStatus(models.Model):
    """Status model for the Store model. It contains all possible statuses
    of a store in the system e.g. Active, Inactive, Deleted etc."""

    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10, null=False)


class Store(models.Model):
    """The Store model for harri project. All stores created are
    contained in this model.
    """

    name = models.CharField(max_length=150, null=False)
    owner_name = models.CharField(max_length=150, null=False)
    location = models.CharField(max_length=250, null=True)

    status = models.ForeignKey(StoreStatus, null=False, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StoreItem(models.Model):
    """All items for sale in a store are contained in this model"""

    name = models.CharField(max_length=150, null=False)
    barcode = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    quantity_available = models.IntegerField()

    store = models.ForeignKey(Store, null=False, on_delete=models.CASCADE)

