// Copyright (c) 2016, Havenir and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Goods In Transit"] = {
	"filters": [
        {
			'label': 'Name',
			'fieldname': 'name',
			'fieldtype': 'Link',
			'options': 'Goods In Transit Note'
			
			
		},
		{
			'label': 'Status',
			'fieldname': 'status',
			'fieldtype': 'Select',
			'options' : 'Draft\nTo Receive\nPartially Received\nReceived'
			
		},
		{
			'label': 'Date',
			'fieldname': 'posting_date',
			'fieldtype': 'Date',
			
		},
		{
			"fieldname": "show_goods_in_transit_item",
			"label": __("Show Goods In Transit Item"),
			"fieldtype": "Check",
			"default": 1,
			on_change: () => {
				$('button[data-label="Refresh"]').click();
			}
		},
		
	]
	
};
