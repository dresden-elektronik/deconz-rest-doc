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


url = "https://raw.githubusercontent.com/dresden-elektronik/deconz-rest-plugin/master/button_maps.json"
#url = "https://raw.githubusercontent.com/manup/deconz-rest-plugin/master/button_maps.json"

f = urlopen(url)

rsp = json.loads(f.read())

actionNames = {
    "S_BUTTON_ACTION_INITIAL_PRESS": "Initial press",
    "S_BUTTON_ACTION_HOLD": "Hold",
    "S_BUTTON_ACTION_SHORT_RELEASED": "Short release",
    "S_BUTTON_ACTION_LONG_RELEASED": "Long release",
    "S_BUTTON_ACTION_DOUBLE_PRESS": "Double press",
    "S_BUTTON_ACTION_TREBLE_PRESS": "Treeble press",
    "S_BUTTON_ACTION_QUADRUPLE_PRESS": "Quadruple press",
    "S_BUTTON_ACTION_SHAKE": "Shake",
    "S_BUTTON_ACTION_DROP": "Drop",
    "S_BUTTON_ACTION_TILT": "Tilt",
    "S_BUTTON_ACTION_MANY_PRESS": "Many press"
}

print("# Button Events\n")
print("This page was auto generated from [button_maps.json](" + url + ")\n")
print('The following sections enumerate supported values for `state.buttonevent` for [/sensors](../../sensors) of type ZHASwitch.\n')


def print_button(btnArr, buttons, buttons1, actions, acc):
	btn = btnArr[5] # button ref in array
	action = btnArr[6] # action ref in array

    #"buttons": [
    #    {"S_BUTTON_1": "Top left button"},
    #    {"S_BUTTON_2": "Bottom left button"},
    #    {"S_BUTTON_3": "Top right button"},
    #    {"S_BUTTON_4": "Bottom right button"}
    #]


	if "S_BUTTON" in btn and "_ACTION_" in action and action in actionNames:
		val = buttons[btn] + actions[action]

		extra = "Button {0}".format(int(buttons[btn] / 1000))  # 4000 --> 4

		if buttons1:
			for x in buttons1:
				if btn in x:
					extra = x[btn]

		if val not in acc:
			acc.append(val)
			print("| {0:14d} | {1:16s} | {2:<24s} |".format(val, actionNames[action], extra)) # btnArr[-1]

	return acc


def print_buttons(key, rsp):

	print("| {0:<14s} | {1:<16s} | {2:<24s} |".format("Value", "Action", "Button"))
	print("|----------------|------------------|--------------------------|")

	acc = []

	obj = rsp["maps"][key]

	buttons1 = [ ]
	if "buttons" in obj:
		buttons1 = obj["buttons"];


	for btn in obj["map"]:

		acc = print_button(btn, rsp["buttons"], buttons1, rsp["buttonActions"], acc)

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
