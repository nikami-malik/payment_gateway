# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

import frappe
import json
# import xendit

@frappe.whitelist(allow_guest=True)
def invoice_terbayar():
    return 'Success'
