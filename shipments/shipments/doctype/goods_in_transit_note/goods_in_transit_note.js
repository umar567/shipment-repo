// Copyright (c) 2020, Havenir and contributors
// For license information, please see license.txt

frappe.ui.form.on('Goods In Transit Note', {
	calculate_amount: function (frm){
		// triggers when you change row value in Goods In Transit Note Item
		let doc = frm.doc;
		let qty_total = 0;
		let amount_total = 0;
		for (let i in doc.items){
			if (doc.items[i].qty && doc.items[i].rate){
			doc.items[i].total_amount = (doc.items[i].qty)*(doc.items[i].rate);
			frm.refresh_field('items');
		}
		qty_total += doc.items[i].qty;
		amount_total += doc.items[i].total_amount
		}
		frm.set_value('total_qty', qty_total);
		frm.set_value('amount', amount_total);
	},
});

frappe.ui.form.on('Goods In Transit Item', {
	
	
	
	
	qty: function(frm, cdt, cdn) {
		
		frm.trigger('calculate_amount');
	},

	rate: function(frm, cdt, cdn) {
		
		frm.trigger('calculate_amount');	
	},
});

