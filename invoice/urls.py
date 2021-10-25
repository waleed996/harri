"""
All urls related to invoice are defined here

"""


from django.urls import path

from invoice.views import InvoiceView, StoreInvoiceReportView


urlpatterns = [

    # Invoice View
    path("store/order/invoice", InvoiceView.as_view()),


    # Invoice Report View
    path("report/invoice", StoreInvoiceReportView.as_view())


]

