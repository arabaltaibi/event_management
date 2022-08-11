# -*- coding: utf-8 -*-
# Copyright (c) 2022, Venture Force Global and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import pyqrcode
import textwrap

class Guest(Document):
	def validate(self):
		if not self.qrcode_file:
			txt = """Dear {0} you are invited by {1} on {2}.""".format(self.guest,self.invited_by,self.event)
			Qrtext = pyqrcode.create(textwrap.dedent(txt))
			Qrtext.svg('/home/frappe/frappe-bench/sites/site1.local/public/files/'+self.name+'.svg', scale=8)
			self.qrcode_file='/files/'+self.name+'.svg'
	def set_invited_members(self):
		doc = frappe.get_doc('Events', self.event)
		member = doc.append('invited_members')
		member.guest_id = self.name
		member.guest = self.guest
		member.invited_by = self.invited_by
		member.phone_no = self.phone_no
		member.mobile_no = self.mobile_no
		member.email = self.email
		if self.rsvp == 1:
			member.rsvp = "Yes"
			member.response = self.response
			member.respond_status = self.respond_status
			member.rsvp_comments = self.rsvp_comments
		else:
			member.rsvp = "No"
		doc.save()


