# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

import frappe

def create_xendit(self, method):
    if self.custom_payment_gateway == "Xendit":
        import xendit
        from xendit.apis import InvoiceApi
        from payment_gateway.xendit.utils import xendit_auth
        
        api_client = xendit_auth()

        # Create an instance of the API class
        api_instance = InvoiceApi(api_client)

        create_invoice_request = {
            "external_id": self.name,
            "amount": self.grand_total,
            "description": self.remarks,
            "items": get_so_detail(self.items),
            "fees": [
                {
                    "type": "Biaya Aplikasi",
                    "value": 4000
                }
            ],
            "fixed_va": False,
            "invoice_duration": "3600"
        }
        
        if self.custom_payment_gateway_method:
            xendit_metod = frappe.db.get_value("Mode of Payment", self.custom_payment_gateway_method, "xendit_name")
            if not xendit_metod:
                frappe.throw("Mode of Payment {} tidak memiliki method untuk pembayaran Xendit".format(self.custom_payment_gateway_method))

            create_invoice_request.update({
                "payment_methods": [xendit_metod],
            })

        try:
            # Create an invoice
            api_response = api_instance.create_invoice(create_invoice_request)
            self.custom_xendit_id = api_response["id"]
            self.custom_payment_url = api_response["invoice_url"]
            self.db_update()
        except xendit.XenditSdkException as e:
            frappe.throw("Gagal Menghubungkan dengan Xendit")
    elif self.custom_payment_gateway == "Midtrans":
        from payment_gateway.midtrans.utils import midtrans_snap

        snap = midtrans_snap()
        param = {
            "transaction_details": {
                "order_id": self.name,
                "gross_amount": self.grand_total
            }, 
            "item_details": get_so_detail(self.items),
            "credit_card":{
                "secure" : True
            }
        }

        try:
            transaction = snap.create_transaction(param)
            self.custom_midtrans_token = transaction["token"]
            self.custom_payment_url = transaction["redirect_url"]
            self.db_update()
            # create transaction
        except Exception as e:
            frappe.throw(str(e))

def get_so_detail(items):
    ress = []
    for row in items:
        item = {
            "id": row.item_code,
            "name": row.item_name,
        }

        if row.so_detail:
            so_detail = frappe.db.get_value("Sales Order Item", row.so_detail, ["price_list_rate", "qty"], as_dict=1)
            item.update({
                "price": so_detail.price_list_rate,
                "quantity": so_detail.qty,
            })
        else:
            item.update({
                "price": row.price_list_rate,
                "quantity": row.qty,
            })
       
    return ress