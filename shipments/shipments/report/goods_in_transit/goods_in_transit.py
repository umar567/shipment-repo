# Copyright (c) 2013, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters):
	columns, data = [], []
	columns = [{
	"fieldname": "name",
	"label": _("ID"),
	"fieldtype": "Link",
	"options": "Goods In Transit Note",
	
	
	},
	{
	"fieldname": "posting_date",
	"label": _("Date"),
	"fieldtype": "date",
	"width": "80"
	
	},
	{
		"fieldname": "invoiced_by",
		"label": _("Invoiced By"),
		"fieldtype": "Link",
		"options": "Supplier",
		"width": "90"
	
	}]
	if filters.show_goods_in_transit_item:
			columns.extend([{
		"fieldname": "item_code",
		"label": _("Item Code"),
		"fieldtype": "Data",
		
	},
	{
		"fieldname": "warehouse",
		"label": _("warehouse"),
		"fieldtype": "Data",
		
		
	},
	{
		"fieldname": "qty",
		"label": _("Qty"),
		"fieldtype": "Float",
		
		
	},
	{
		"fieldname": "rate",
		"label": _("Rate"),
		"fieldtype": "Float",
		
		
	},
	{
		"fieldname": "amount",
		"label": _("Amount"),
		"fieldtype": "Currency",
		"width": "100"
		
		
	}

			])
	
	columns.extend([{
		"fieldname": "invoiced_to",
		"label": _("Invoiced To"),
		"fieldtype": "Link",
		"options": "Company",
		"width": "130"
		
	},
	{
		"fieldname": "company",
		"label": _("Company"),
		"fieldtype": "Link",
		"options": "Company",
		"width": "130"
		
		
	},
	{
		"fieldname": "pol",
		"label": _("POL"),
		"fieldtype": "Link",
		"options": "Port Of Loading",
		"width": "100"
	},
	{
		"fieldname": "etd",
		"label": _("ETD"),
		"fieldtype": "Date",
		"width": "100"
	},
	{
		"fieldname": "pod",
		"label": _("POD"),
		"fieldtype": "Link",
		"options": "Point Of Delivery",
		"width": "100"
		
	},
	{
		"fieldname": "eta",
		"label": _("ETA"),
		"fieldtype": "data",
		"width": "100"
		
	},
	{
		"fieldname": "vesselvehicle",
		"label": _("Vessel/Vehicle"),
		"fieldtype": "Link",
		"options": "Vessel",
		"width": "100"
	},
	{
		"fieldname": "cntr_no",
		"label": _("CNTR No."),
		"fieldtype": "Data",
		
	},
	{
		"fieldname": "status",
		"label": _("Status"),
		"fieldtype": "Select",
		"width": "100"
		# 'options' : 'Draft\nWaiting to Receive Items\nReceived'
		
	}
	])
	
	data = get_data(filters)
	return columns,data
def get_data(filters):
	q_filters = {}
	data = []
	for key, value in filters.items():
		if key not in ['show_goods_in_transit_item']:
			q_filters[key] = value

	doclist = frappe.db.get_list('Goods In Transit Note',q_filters)
	for x in doclist:
		docname = x.name
		doc = frappe.get_doc('Goods In Transit Note', docname)
		
		if filters.show_goods_in_transit_item:
			for y in doc.items:
				data.append({
					'name' : doc.name,
					'posting_date' : doc.posting_date,
					'invoiced_by' : doc.invoiced_by,
					'invoiced_to': doc.invoiced_to,
					'item_code' : y.item_code, 
					'warehouse' : y.warehouse,
					'qty' : y.qty,
					'rate' : y.rate,
					'amount' : y.amount,
					'company' : doc.company, 
					'pol' : doc.pol,
					'etd' : doc.etd, 
					'pod' : doc.pod,
					'eta' : doc.eta,
					'vesselvehicle' : doc.vesselvehicle,
					'cntr_no' : doc.cntr_no,
					'status' : doc.status
				})
		else:
			data.append({
				'name' : doc.name,
				'date' : doc.date,
				'invoiced_by' : doc.invoiced_by,
				'invoiced_to': doc.invoiced_to,
				'company' : doc.company, 
				'pol' : doc.pol,
				'etd' : doc.etd, 
				'pod' : doc.pod,
				'eta' : doc.eta,
				'vesselvehicle' : doc.vesselvehicle,
				'cntr_no' : doc.cntr_no,
				'status' : doc.status
			})
				
	return data