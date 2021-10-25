"""
All views related to invoices are contained here

"""


from rest_framework.views import APIView

from invoice.invoice_controller import InvoiceController, InvoiceReportViewController


class InvoiceView(APIView):
    """CRUD API view for invoice"""


    invoice_controller = InvoiceController()


    def post(self, request):
        """Create API for Invoice"""

        return self.invoice_controller.create_invoice(request)


    def get(self, request):
        """GET API for Invoice"""

        pass


class StoreInvoiceReportView(APIView):
    """API view for invoice report of a store"""


    invoice_report_controller = InvoiceReportViewController()


    def get(self, request):
        """GET invoices report API"""

        return self.invoice_report_controller.list_invoice_details_by_params(request)

