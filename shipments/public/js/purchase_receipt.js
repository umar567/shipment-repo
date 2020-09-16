frappe.ui.form.on("Purchase Receipt", {

    refresh: function(frm) {
    //Add custom button Get Items From
		if (frm.is_new()){
			frm.add_custom_button(__('Get Items'), () => frm.trigger('get_items_from_goodsintransit'), __('Goods In Transit'));
			
        }
    },
    //Add custom function
	get_items_from_goodsintransit: function (frm) {
		if (!frm.doc.supplier){
			frappe.msgprint('Supplier not selected')
		}
		else{
		new frappe.ui.form.MultiSelectDialog({
			doctype: "Goods In Transit Note",
			target: cur_frm,
			setters: {
				company: cur_frm.doc.company,
				
			},
			date_field: "date",
			get_query() {
				return {
					filters: { 
						docstatus: ['=', 1],
						invoiced_by: cur_frm.doc.supplier
					}
				}
			},
			action(selections) {
				if (selections.length == 0){
					frappe.msgprint('Select Goods In Transit Note')
				}
				else{
					cur_frm.doc.items = null
					frappe.call('shipments.events.purchase_receipt.get_items_from_goodsintransit',{selections})
					cur_frm.refresh();
				}
			}
		});
	}
	}
});