# -*- coding: utf-8 -*-
# Copyright (c) 2020, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime

class GoodsInTransitNote(Document):
	def get_items_from_purchase_order(self,selections):
		
		total_qty = 0
		amount = 0
		self.items = []
		for i in selections:
			purchase_order = frappe.get_doc('Purchase Order', i)
			for item in purchase_order.items:
				self.append('items',{
					'item_code' : item.item_code,
					'qty': item.qty,
					'rate': item.rate,
					'total_amount' : item.amount,
					'warehouse'	: item.warehouse,
					'conversion_factor' : item.conversion_factor,
					'uom' : item.uom
				}
				)
				total_qty += item.qty
				amount += item.amount
		self.total_qty = total_qty
		self.amount = amount
				
		
		

		 
		
	
