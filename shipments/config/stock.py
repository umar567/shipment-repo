from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Stock Transactions"),
			"items": [
                {
					"type": "doctype",
					"name": "Goods In Transit Note",
					"onboard": 1,
					"dependencies": ["Item"],
				}
            ]
        },
        {
			"label": _("Stock Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Goods In Transit",
					"doctype": "Goods In Transit Note",
					"onboard": 1
					
				}
            ]
        }
    ]