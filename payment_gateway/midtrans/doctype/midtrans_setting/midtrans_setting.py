# Copyright (c) 2024, Nikahmi and contributors
# For license information, please see license.txt

# import frappe
# import midtransclient

# from midtransclient.config import ApiConfig
# from midtransclient.http_client import HttpClient
from frappe.model.document import Document


class MidtransSetting(Document):
	pass
	# def validate(self):
	# 	self.api_config = ApiConfig(self.is_production,self.server_key,self.client_key)
	# 	self.http_client = HttpClient()

	# 	api_url = self.api_config.get_core_api_base_url() + '/v2/token'
		

	# 	try:
	# 		response_dict, response_object = self.http_client.request(
	# 			'get',
	# 			self.api_config.server_key,
	# 			api_url,
	# 			{
	# 				"client_key": self.client_key,
	# 				"card_number": "4811 1111 1111 1114"
	# 			}
	# 		)
	# 		frappe.throw(str(response_dict))
	# 		# frappe.msgprint("Midtrans Berhasil Terhubung dengan Balance sebesar {}".format(fmt_money(response["balance"], currency=currency)))
	# 	except midtransclient.MidtransAPIError as e:
	# 		frappe.throw("Api Key Midtrans tidak datap ditemukan")
