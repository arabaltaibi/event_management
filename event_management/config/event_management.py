from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
            "label": _("Event Registration"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Events",
                    "label": _("Events"),
                    "description": _("Events"),
					"onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Event Registration",
                    "label": _("Event Registration"),
                    "description": _("Event Registration")
                },
                {
                    "type": "doctype",
                    "name": "Organization",
                    "label": _("Organization"),
                    "description": _("Organization")
                },
                {
                    "type": "doctype",
                    "name": "Guest",
                    "label": _("Guest"),
                    "description": _("Guest")
                },
                {
                    "type": "doctype",
                    "name": "City",
                    "label": _("City"),
                    "description": _("City")
                },
                {
                    "type": "doctype",
                    "name": "Country",
                    "label": _("Country"),
                    "description": _("Country")
                },

            ]
        }
	]