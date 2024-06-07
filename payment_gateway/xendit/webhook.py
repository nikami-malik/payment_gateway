# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

import frappe
import json
# import xendit

@frappe.whitelist(allow_guest=True)
def invoice_terbayar():
    frappe.session.user = "Administrator"
    payload = json.loads(frappe.request.data.decode('utf-8'))

    doc = frappe.new_doc("Xendit Webhook Log")
    if payload["status"] == "PAID":
        doc.type = "Invoice Terbayar",
    else:
        doc.type = "Invoice Gagal Dibayar"

    doc.update({
        "payload": frappe.as_json(payload)
    })

    doc.data_payload = payload
    doc.save()

    return 'Success'