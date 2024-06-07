# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

import frappe
import midtransclient

def midtrans_snap(server_key = None):
    if not server_key:
        server_key = frappe.db.get_single_value("Midtrans Setting", "server_key")

    if not server_key:
        frappe.throw("Isi Api Key Midtrans terlebih dahulu")

    snap = midtransclient.Snap(
        # Set to true if you want Production Environment (accept real transaction).
        is_production=False,
        server_key=server_key
    )
    
    return snap