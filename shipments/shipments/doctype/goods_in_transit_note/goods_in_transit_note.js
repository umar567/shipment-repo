// Copyright (c) 2020, Havenir and contributors
// For license information, please see license.txt

frappe.ui.form.on('Goods In Transit Note', {

	refresh: function(frm) {
			
		if (frm.is_new()){
			frm.add_custom_button(__('Get items from purchase order'), 
			() => frm.trigger('get_items_from_purchase_order'), __('Get Items'));
			
		}
		if (cur_frm.doc.docstatus == 1 && cur_frm.doc.status != 'Received'){
		frm.add_custom_button('Create purchase receipt', () => {
			let doc = frm.doc
			frappe.run_serially([
				() => frappe.new_doc('Purchase Receipt'),
				() => {
					cur_frm.doc.supplier = doc.invoiced_by;
					for (let i in doc.items){
						cur_frm.doc.items = []
						cur_frm.add_child('items', {
							item_code : doc.items[i].item_code,
							item_name: doc.items[i].item_name,
							description: doc.items[i].description,
							warehouse: doc.items[i].warehouse,
							qty : doc.items[i].qty - doc.items[i].received_qty,
							uom : doc.items[i].uom,
							conversion_factor: doc.items[i].conversion_factor,
							stock_uom: doc.items[i].stock_uom,
							rate : doc.items[i].rate,
							amount : doc.items[i].amount,
							goods_in_transit_note: doc.name,
							goods_in_transit_note_item: doc.items[i].name
						})
					}
					cur_frm.refresh_field('items')
				}
			]);
		});
	}

	
		
	},

	get_items_from_purchase_order: function (frm) {
		if (!frm.doc.invoiced_by){
			frappe.msgprint('Invoiced By not selected')
		}
		else{
		new frappe.ui.form.MultiSelectDialog({
			doctype: "Purchase Order",
			target: cur_frm,
			setters: {
				company: cur_frm.doc.company,
				
			},
			date_field: "posting_date",
			get_query() {
				return {
					filters: { 
						docstatus: ['=', 1],
						supplier: cur_frm.doc.invoiced_by,
						goods_status:["!=", "Dispatched"]
					}
				}
			},
			action(selections) {
				console.log(selections[0])
				if (selections.length == 0){
					frappe.msgprint('Select a Purchase Order')
				}
				else{
					cur_frm.doc.items = null
					frm.call('get_items_from_purchase_order',selections)
					cur_frm.refresh();
					cur_frm.trigger('calculate_amount');
				}
			}
		});
	}
	},

	calculate_amount: function (frm){
		// triggers when you change row value in Goods In Transit Note Item
		let doc = frm.doc;
		let qty_total = 0;
		let amount_total = 0;
		for (let i in doc.items){
			if (doc.items[i].qty && doc.items[i].rate){
				doc.items[i].amount = (doc.items[i].qty)*(doc.items[i].rate);
				amount_total += doc.items[i].amount;
			}
			if (doc.items[i].qty){
				qty_total += doc.items[i].qty;
			}		
		}
		frm.refresh_field('items');
		frm.set_value('total_qty', qty_total);
		frm.set_value('total', amount_total);
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

