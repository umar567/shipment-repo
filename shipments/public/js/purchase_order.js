frappe.ui.form.on("Purchase Order", {
    //add custom function
	before_submit: function(frm) {
		let doc = frm.doc;
		doc.goods_status = "Goods pending for departure"
	  },
	// Add Custom Button Goods In Transit
	refresh: function(frm) {
		if (cur_frm.doc.docstatus == 1){
			frm.add_custom_button('Goods In Transit', () => {
				let doc = frm.doc
				frappe.run_serially([
					() => frappe.new_doc('Goods In Transit Note'),
					() => {
						cur_frm.doc.invoiced_by = doc.supplier;
						cur_frm.refresh_field('invoiced_by')
						console.log(cur_frm.doc.invoiced_by)
						cur_frm.doc.items = []
						for (let i in doc.items){
							cur_frm.add_child('items', {
								item_code : doc.items[i].item_code,
								item_name: doc.items[i].item_name,
								description: doc.items[i].description,
								warehouse: doc.items[i].warehouse,
								qty : doc.items[i].qty,
								uom : doc.items[i].uom,
								conversion_factor: doc.items[i].conversion_factor,
								stock_uom: doc.items[i].stock_uom,
								rate : doc.items[i].rate,
								amount : doc.items[i].amount,
								purchase_order: doc.name,
								purchase_order_item: doc.items[i].name
							})
						}
						cur_frm.refresh_field('items');
						cur_frm.trigger('calculate_amount');
					}
				]);
			}, __("Create"));
		}
	},
});