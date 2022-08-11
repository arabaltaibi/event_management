// Copyright (c) 2022, Venture Force Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('People', {
	refresh(frm){
	$(".btn-new-email").hide()
	},
	before_save(frm) {
		frm.set_value("full_name", frm.doc.first_name + " " + frm.doc.last_name  + " " + frm.doc.alias);
	}
})