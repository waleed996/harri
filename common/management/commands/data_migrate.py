"""
Management command that migrates static data in database tables

"""


from django.core.management.base import BaseCommand
from invoice.models import InvoiceStatus
from order.models import OrderStatus

from store.models import StoreStatus


class Command(BaseCommand):
    help = "Run Data Migrations For Static Data For Harri Service"

    def handle(self, *args, **kwargs):


        """Static Data for StoreStatus model"""

        StoreStatus.objects.create(
            name="Active",
            code="A"
        )
        StoreStatus.objects.create(
            name="InActive",
            code="IA"
        )
        StoreStatus.objects.create(
            name="Deleted",
            code="D"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated for model: StoreStatus"))




        """Static Data for InvoiceStatus model"""

        InvoiceStatus.objects.create(
            name="Paid",
            code="P"
        )
        InvoiceStatus.objects.create(
            name="UnPaid",
            code="UP"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated for model: InvoiceStatus"))





        """Static Data for OrderStatus model"""

        OrderStatus.objects.create(
            name="Order Placed",
            code="OP"
        )
        OrderStatus.objects.create(
            name="Pending",
            code="PEN"
        )
        OrderStatus.objects.create(
            name="Shipped",
            code="S"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated for model: OrderStatus"))

