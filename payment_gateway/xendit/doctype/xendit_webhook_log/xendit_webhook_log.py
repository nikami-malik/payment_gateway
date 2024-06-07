# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt
import json
from datetime import datetime

import frappe
from frappe.utils import getdate
from frappe.model.document import Document

class XenditWebhookLog(Document):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if self.payload:
			self.data_payload = json.loads(self.payload) 

	def validate(self):
		if self.data_payload["status"] == "PAID":
			self.type = "Invoice Terbayar"

	def after_insert(self):
		
		if self.type == "Invoice Terbayar":
			from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry
			timestamp_str = self.data_payload["paid_at"]
			datetime_obj = datetime.fromisoformat(timestamp_str[:-1])
			data = getdate(datetime_obj)

			payment = get_payment_entry("Sales Invoice", self.data_payload["external_id"])
			payment.posting_date = getdate(datetime_obj)
			payment.custom_xendit_payment_id = self.data_payload["external_id"]
			payment.reference_date = getdate(datetime_obj)
			payment.reference_no = self.data_payload["payment_id"]
			payment.submit()