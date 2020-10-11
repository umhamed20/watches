
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{	
			"label": _("Watches"),
            "icon": "octicon octicon-briefcase",
           	"label": _("watch"),
			"items": [
				{
					"type": "doctype",
                   	"name": "watch name",
                    "label": _("watch name"),
				},
				{
					 "type": "doctype",
                    "name": "watch modle",
                    "label": _("watch modle"),
				}
			]
		},
	
	]

