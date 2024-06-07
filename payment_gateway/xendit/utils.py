# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

import frappe
import xendit

def xendit_auth(token = None):
    if not token:
        token = frappe.db.get_single_value("Xendit Settings", "token")

    if not token:
        frappe.throw("Isi Api Key Xendit terlebih dahulu")

    xendit.set_api_key(token)
    client = xendit.ApiClient()

    return client