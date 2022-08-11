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
                    "name": "Guest",
                    "label": _("Guest"),
                    "description": _("Guest")
                },

            ]
		},
		{
			"label": _("Master Data"),
			"items": [
				{
					"type": "doctype",
					"name": "Organization",
					"description": _("Organization"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Country",
					"description": _("Country"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "City",
					"description": _("City"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Team",
					"description": _("Team"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Vertical",
					"description": _("Vertical"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Catering Vendor",
					"description": _("Catering Vendor"),
					"onboard": 1,
				},

			]
		},
		{
			"label": _("People/ Volunteers /Tags"),
			"items": [
				{
					"type": "doctype",
					"name": "People",
					"description": _("People"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Volunteers",
					"description": _("Volunteers"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("Contacts of People"),
                    "label": _("Contacts of People"),
					"onboard": 1,
				},

			]
		},

	]