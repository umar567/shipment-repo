# -*- coding: utf-8 -*-
# Copyright (c) 2020, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime

class GoodsInTransitNote(Document):
	def validate(self):
		self.calculate_item_total()

	def on_submit(self):
		self.db_set('status', 'Waiting to Receive Items')
		self.update_purchase_order_items()

	def on_cancel(self):
		self.update_purchase_order_on_cancel()
		

	def calculate_item_total(self):
		total_qty = 0
		total_amount = 0
		for row in self.items:
			total_qty += row.qty
			total_amount += row.amount
		
		self.total_qty = total_qty
		self.amount = total_amount

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
				self.update_purchase_order_goods_status(row)
	
	def update_purchase_order_goods_status(self, row):
		''' updates Purchase Order Goods Status 
			Goods Status = [To Dispatch, Partially Dispatched, Dispatched]
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
		elif total_dispatched_qty == 0:
			purchase_doc.db_set('goods_status', 'To Dispatch')
		else:
			purchase_doc.db_set('goods_status', 'Partially Dispatched')
		
	def update_purchase_order_on_cancel(self):
		for row in self.items:
			if row.purchase_order:
				dispatched_qty = frappe.db.get_value('Purchase Order Item', 
				{'name': row.purchase_order_item}, 
				['dispatched_qty'])

				new_dispatched_qty = dispatched_qty - row.qty
				frappe.db.set_value(
					'Purchase Order Item', 
					row.purchase_order_item, 
					'dispatched_qty', 
					new_dispatched_qty
				)
				self.update_purchase_order_goods_status(row)

	def get_items_from_purchase_order(self,selections):
		total_qty = 0
		amount = 0
		for doc_id in selections:
			purchase_order = frappe.get_doc('Purchase Order', doc_id)
			for row in purchase_order.items:
				if row.qty - row.dispatched_qty != 0:
					qty = row.qty - row.dispatched_qty
					item_amount = row.rate * qty
					self.append('items',{
						'item_code' :row.item_code,
						'item_name': row.item_name,
						'description': row.description,
						'warehouse': row.warehouse,
						'qty' :row.qty - row.dispatched_qty,
						'uom' :row.uom,
						'conversion_factor': row.conversion_factor,
						'stock_uom': row.stock_uom,
						'rate' :row.rate,
						'amount' :row.rate * qty,
						'purchase_order': purchase_order.name,
						'purchase_order_item': row.name
					})
					total_qty += qty
					amount += item_amount
		self.total_qty = total_qty
		self.total = amount

	

				
		
		

		 
		
	
