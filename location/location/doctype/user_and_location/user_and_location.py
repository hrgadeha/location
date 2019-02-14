# -*- coding: utf-8 -*-
# Copyright (c) 2019, Hardik Gadesha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class UserAndLocation(Document):
	pass

@frappe.whitelist(allow_guest=True)
def getUserLocation(user):
	location = frappe.get_value('User And Location', user, 'location')
	return location
