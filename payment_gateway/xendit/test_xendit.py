import time
import xendit
from xendit.apis import InvoiceApi
from xendit.invoice.model.invoice_not_found_error import InvoiceNotFoundError
from xendit.invoice.model.invoice import Invoice
from xendit.invoice.model.bad_request_error import BadRequestError
from xendit.invoice.model.unauthorized_error import UnauthorizedError
from xendit.invoice.model.forbidden_error import ForbiddenError
from xendit.invoice.model.create_invoice_request import CreateInvoiceRequest

from payment_gateway.xendit.utils import xendit_auth

def create_invoice():
    api_client = xendit_auth()

    # Create an instance of the API class
    api_instance = InvoiceApi(api_client)
    create_invoice_request = {
		"external_id": "external_id_example",
		"amount": 300000,
		"description": "Tes",
		"fixed_va": False,
		"invoice_duration": "86400"
	}

    # example passing only required values which don't have defaults set
    try:
        # Create an invoice
        api_response = api_instance.create_invoice(create_invoice_request)
        print(api_response)
    except xendit.XenditSdkException as e:
        print("Exception when calling InvoiceApi->create_invoice: %s\n" % e)

