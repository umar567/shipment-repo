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
								qty : doc.items[i].qty,
								warehouse : doc.items[i].warehouse,
								rate : doc.items[i].rate,
								total_amount : doc.items[i].amount,
							})
						}
						cur_frm.refresh_field('items')
					}
				]);
			});
		}
	},
});