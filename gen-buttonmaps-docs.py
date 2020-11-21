#!/usr/bin/env python
"""
Snipped to download current button map JSON file and genrate a Markdown documentation page.
compatible with python 3.

To invoke this script run make.
"""

import os
import json
try:
	from urllib.request import urlopen, urlretrieve
except ImportError:
	from urllib2 import urlopen
	from urllib import urlretrieve


#url = "https://raw.githubusercontent.com/dresden-elektronik/deconz-rest-plugin/master/button_maps.json"
url = "https://raw.githubusercontent.com/manup/deconz-rest-plugin/button_maps/button_maps.json"

f = urlopen(url)

rsp = json.loads(f.read())

print("# Button Maps\n")
print("This page was auto generated from [button_maps.json](" + url + ")\n")
print('The following sections enumerate supported values for `state.buttonevent` for sensors of type ZHASwitch.\n')


def print_button(btnArr, buttons, actions):
	btn = btnArr[5] # button ref in array
	action = btnArr[6] # action ref in array

	if "S_BUTTON" in btn and "_ACTION_" in action:
		val = buttons[btn] | actions[action]
		print("| {0:14d} | {1:<34s} |".format(val, btnArr[-1]))


def print_buttons(key, rsp):

	print("| {0:<14s} | {1:<34s} |".format("Value", "Description"))
	print("|----------------|------------------------------------|")

	for btn in rsp["maps"][key]["map"]:
		print_button(btn, rsp["buttons"], rsp["buttonActions"])

	print('\n')



def print_modelids(key, bm):
	print('## ' + bm["vendor"] + ' ' + bm["doc"] + '\n')
	print('**Model identifiers**\n\n')

	print('<ul class="value-list">')

	for mdlid in bm["modelids"]:
		print('<li>"' + mdlid + '"</li>')

	print('</ul>\n')

def print_button_map(key, rsp):
	print_modelids(key, rsp["maps"][key])
	print_buttons(key, rsp)

for key in rsp["maps"]:
	print_button_map(key, rsp)
