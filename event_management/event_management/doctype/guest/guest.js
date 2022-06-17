// Copyright (c) 2022, Venture Force Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('Guest', {
	refresh(frm) {
		// your code here
		  if (!frm.doc.barcode_id){
             frm.set_value("barcode_id",frm.doc.name)
	    }
	},
	validate(frm){
	  
	}
})