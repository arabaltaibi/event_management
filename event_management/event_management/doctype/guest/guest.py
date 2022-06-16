# -*- coding: utf-8 -*-
# Copyright (c) 2022, Venture Force Global and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
import pyqrcode
import textwrap

class Guest(Document):
	def validate(self):
		if not self.qrcode_file:
			txt = """Dear {0} you are invited by {1} on {2}.""".format(self.guest,self.invited_by,self.event)
			Qrtext = pyqrcode.create(textwrap.dedent(txt))
			Qrtext.svg('/home/frappe/frappe-bench/sites/client.tboss.info/public/files/'+self.name+'.svg', scale=8)
			self.qrcode_file='/files/'+self.name+'.svg'



