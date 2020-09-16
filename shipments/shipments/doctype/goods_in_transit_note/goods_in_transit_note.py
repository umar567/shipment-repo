# -*- coding: utf-8 -*-
# Copyright (c) 2020, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime

class GoodsInTransitNote(Document):
	def on_submit(self):
		self.update_purchase_order_items()

	def update_purchase_order_items(self):
		'''validating items from the purchase order if they are still available'''		
		for row in self.items:
			if row.purchase_order:
				qty, dispatched_qty = frappe.db.get_value('Purchase Order Item', 
				{'name': row.purchase_order_item}, 
				['qty', 'dispatched_qty'])

				if (qty - dispatched_qty < row.qty):
					frappe.throw(f'Row# {row.idx}: {row.qty} quantity not available for item {row.item_code}')
				
				new_dispatched_qty = dispatched_qty + row.qty
				frappe.db.set_value('Purchase Order Item', row.purchase_order_item, 'dispatched_qty', new_dispatched_qty)
				self.update_purchase_order__goods_status(row)
	
	def update_purchase_order__goods_status(self, row):
		''' updates Purchase Order Goods Status 
			Goods Status = [Partially Dispatched, Dispatched]
			if all goods dispatched then goods status = Dispatched
			if some goods dispatched then goods status = Partially Dispatched
		'''

		#Getting Purchase order document
		purchase_doc = frappe.get_doc('Purchase Order', row.purchase_order)
		total_dispatched_qty = 0
		for row in purchase_doc.items:
			total_dispatched_qty += row.dispatched_qty
		
		if total_dispatched_qty == purchase_doc.total_qty:
			purchase_doc.db_set('goods_status', 'Dispatched')
		else:
			purchase_doc.db_set('goods_status', 'Partially Dispatched')
		

	def get_items_from_purchase_order(self,selections):
		total_qty = 0
		amount = 0
		self.items = []
		for i in selections:
			purchase_order = frappe.get_doc('Purchase Order', i)
			purchase_order.db_set('goods_status', 'Goods in Transit')
			for item in purchase_order.items:
				if item.qty - item.dispatched_qty != 0:
					qty = item.qty - item.dispatched_qty
					item_amount = item.rate * qty
					self.append('items',{
						'item_code' : item.item_code,
						'qty': qty,
						'rate': item.rate,
						'total_amount' : item_amount,
						'warehouse'	: item.warehouse,
						'conversion_factor' : item.conversion_factor,
						'uom' : item.uom,
						'purchase_order': purchase_order.name,
						'purchase_order_item': item.name
					}
					)
					total_qty += qty
					amount += item_amount
		self.total_qty = total_qty
		self.amount = amount

	

				
		
		

		 
		
	
