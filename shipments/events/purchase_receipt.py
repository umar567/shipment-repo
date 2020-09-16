import frappe
#Custom function
@frappe.whitelist()
def get_items_from_goodsintransit(self,selections):
		
		total_qty = 0
		amount = 0
		self.items = []
		for i in selections:
			goods_in_transit = frappe.get_doc('Goods In Transit Note', i)
			for item in goods_in_transit.items:
				self.append('items',{
					'item_code' : item.item_code,
					'qty': item.qty,
					'rate': item.rate,
					'amount' : item.total_amount,
					'warehouse'	: item.warehouse,
					'conversion_factor' : item.conversion_factor,
					'uom' : item.uom
				}
				)
				total_qty += item.qty
				amount += item.total_amount
		self.total_qty = total_qty
		self.total = amount