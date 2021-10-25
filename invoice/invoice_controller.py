"""
Controller for the invoice module. All controllers and business logic
related to invoices is contained here

"""


from django.db.models.aggregates import Count
from invoice.models import Invoice

from invoice.serializers import InvoiceReportSerializer, InvoiceSerializer

from utils.response_utils import create_response, create_message
from utils.request_utils import get_query_param_or_default


class InvoiceController:
    """Controller for the invoice"""

    def create_invoice(self, request):
        """Creates an Invoice

        Args:
            request ([WSGIRequest]): [The request made by the client
                                      for creating invoice]
        """


        try:

            # Serialize the request post data using the serializer
            serialized = InvoiceSerializer(data=request.data)

            # Check if data provided is valid and save
            if serialized.is_valid():

                serialized.save()

            else: # return validation errors to client in case data is invalid

                return create_response(create_message(serialized.errors, 1001), 400)


            return create_response(create_message(serialized.data, 1000), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([], 1002), 500)


class InvoiceReportViewController:
    """Invoice Controller for the report view"""

    def list_invoice_details_by_params(self, request):
        """List invoice report using supported params

        params supported:
        store_id, start_date, end_date

        Args:
            request ([WSGIRequest]): [The request made by the client
                                      for creating invoice]
        """

        try:

            # Store id filter
            if not get_query_param_or_default(request, "store_id", None):
                return create_response(create_message([], 100), 400)

            # Start date filter
            if not get_query_param_or_default(request, "start_date", None):
                return create_response(create_message([], 101), 400)

            # End date fiter
            if not get_query_param_or_default(request, "end_date", None):
                return create_response(create_message([], 102), 400)

            invoices = Invoice.objects.filter(
                created_at__range=[get_query_param_or_default(request, "start_date", None),
                get_query_param_or_default(request, "end_date", None)]
            ).annotate(count=Count('created_at__date')).order_by('created_at__date')

            serialized = InvoiceReportSerializer(invoices, many=True)

            # TODO: change according to the date key format discussed in interview

            return create_response(create_message(serialized.data, 1000), 200)

        except Exception as ex:
            print(ex)
            return create_response(create_message([], 1002), 500)

