// Copyright (c) 2022, Venture Force Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('Guest', {
	refresh(frm) {
			$(".btn-new-email").hide()
		// your code here
		  if (!frm.doc.barcode_id){
             frm.set_value("barcode_id",frm.doc.name)
	    }
	},
	validate(frm){
	  
	}
})

frappe.ui.form.on('Guest', {
    refresh: function(frm) {
      frm.add_custom_button(__('Add Guest in Event'), function(){
       
                frappe.call({
                    method: "set_invited_members",
                   doc:frm.doc
					

                });
		frappe.msgprint(__('Guest Has been added in the Event Sucessfully!'));
		frm.clear_custom_buttons();
    }, __("Add Guest in Event"));

  }
});