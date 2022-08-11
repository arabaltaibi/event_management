# -*- coding: utf-8 -*-
# Copyright (c) 2022, Venture Force Global and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EventRegistration(Document):
	def before_submit(self):
		self.member_attended()
	def member_attended(self):
		doc = frappe.get_doc('Events', self.event_name)
		member = doc.append('attended_members')
		member.guest = self.guest
		member.guest_name = self.guest_name
		member.contact = self.contact
		member.mobile_no = self.mobile_no
		member.phone_no = self.phone_no
		member.check_in_time = self.check_in_time
		member.check_in_by = self.check_in_by
		doc.save()

		
		