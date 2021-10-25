"""
All serializers related to the invoice module are
contained here

"""


from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from invoice.models import Invoice
from order.models import OrderItem

from django.db.models import Sum


class InvoiceSerializer(ModelSerializer):
    """Serializer for the Invoice model"""

    class Meta:
        model = Invoice
        fields = "__all__"



class InvoiceReportSerializer(ModelSerializer):
    """Serializer for the Invoice model"""

    class Meta:
        model = Invoice
        fields = ["items_count", "total_prices"]



    items_count = SerializerMethodField()
    total_prices = SerializerMethodField()


    def get_items_count(self, obj):

        if obj.customer_order:

            return OrderItem.objects.filter(
                customer_order=obj.customer_order
            ).aggregate(Sum("quantity")).get("quantity__sum")


    def get_total_prices(self, obj):

        if obj.customer_order:

            order_items = OrderItem.objects.filter(
                customer_order=obj.customer_order
            )

            total_price = 0
            for item in order_items:
                total_price += item.store_item.price

            return str(total_price)

