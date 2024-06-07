# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

import frappe
import xendit

from frappe.utils import fmt_money
from xendit.apis import BalanceApi
from frappe.model.document import Document


class XenditSettings(Document):
	
	def validate(self):
		from payment_gateway.xendit.utils import xendit_auth
		currency = "IDR"
		try:
			client = xendit_auth(self.token)
			response = BalanceApi(client).get_balance('CASH', currency=currency)
			frappe.msgprint("Xendit Berhasil Terhubung dengan Balance sebesar {}".format(fmt_money(response["balance"], currency=currency)))
		except xendit.XenditSdkException as e:
			frappe.throw("Api Key Xendit tidak dapat ditemukan")