# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cust_acc_mgmt"
app_title = "Customer Account Management"
app_publisher = "Metalman Brewing"
app_description = "Tracking contact activity with customers"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "info@metalmanbrewing.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cust_acc_mgmt/css/cust_acc_mgmt.css"
# app_include_js = "/assets/cust_acc_mgmt/js/cust_acc_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/cust_acc_mgmt/css/cust_acc_mgmt.css"
# web_include_js = "/assets/cust_acc_mgmt/js/cust_acc_mgmt.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
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
# get_website_user_home_page = "cust_acc_mgmt.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cust_acc_mgmt.install.before_install"
# after_install = "cust_acc_mgmt.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cust_acc_mgmt.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cust_acc_mgmt.tasks.all"
# 	],
# 	"daily": [
# 		"cust_acc_mgmt.tasks.daily"
# 	],
# 	"hourly": [
# 		"cust_acc_mgmt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cust_acc_mgmt.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cust_acc_mgmt.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cust_acc_mgmt.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cust_acc_mgmt.event.get_events"
# }

