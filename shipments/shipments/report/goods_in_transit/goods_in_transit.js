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
			'label': 'Document Status',
			'fieldname': 'document_status',
			'fieldtype': 'Select',
			'options' : 'Draft\nWaiting to Receive Items\nReceived'
			
		},
		{
			'label': 'Date',
			'fieldname': 'date',
			'fieldtype': 'Date',
			
		},
		{
			"fieldname": "show_goods_in_transit_item",
			"label": __("Show Goods In Transit Item"),
			"fieldtype": "Check",
			on_change: () => {
				$('button[data-label="Refresh"]').click();
			}
		},
		
	]
	
};
