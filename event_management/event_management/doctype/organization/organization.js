// Copyright (c) 2022, Venture Force Global and contributors
// For license information, please see license.txt

frappe.ui.form.on('Organization', {
	refresh(frm){
$(".btn-new-email").hide()	
},
	before_save(frm) {
		if(frm.doc.alias){
			frm.set_value("org_name", frm.doc.organization_name + " - " + frm.doc.alias);
		}
		else {
			frm.set_value("org_name", frm.doc.organization_name);
		}
		
	}
})