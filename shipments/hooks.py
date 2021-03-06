# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "shipments"
app_title = "shipments"
app_publisher = "Havenir"
app_description = "shipments"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "Havenir"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shipments/css/shipments.css"
# app_include_js = "/assets/shipments/js/shipments.js"

# include js, css files in header of web template
# web_include_css = "/assets/shipments/css/shipments.css"
# web_include_js = "/assets/shipments/js/shipments.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Purchase Order" : "public/js/purchase_order.js",
    "Purchase Receipt" : "public/js/purchase_receipt.js"
}

# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "shipments.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "shipments.install.before_install"
# after_install = "shipments.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shipments.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events


doc_events = {
	"Purchase Receipt": {
		"on_submit": "shipments.events.purchase_receipt.update_goods_in_transit_note_items",
        "on_cancel": "shipments.events.purchase_receipt.update_goods_in_transit_note_items_on_cancel"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shipments.tasks.all"
# 	],
# 	"daily": [
# 		"shipments.tasks.daily"
# 	],
# 	"hourly": [
# 		"shipments.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shipments.tasks.weekly"
# 	]
# 	"monthly": [
# 		"shipments.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "shipments.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shipments.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shipments.task.get_dashboard_data"
# }

