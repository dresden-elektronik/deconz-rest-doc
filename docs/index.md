---
title: Introduction
summary: A brief description of my document.
date: 2020-11-19

---
# Introduction

This documentation describes the deCONZ REST-API, which is provided by the [deCONZ REST-API Plugin](http://github.com/dresden-elektronik/deconz-rest-plugin) on Github that runs a lightweight HTTP server within the [deCONZ](https://phoscon.de/en/conbee2/software#deconz) application on the Raspberry Pi.

The REST-API allows third party applications easy monitoring and control of a Zigbee network from local or remote operating clients.

One of the following devices is needed to get Zigbee support on the Raspberry Pi or PC.

* [RaspBee](https://phoscon.de/raspbee) and [RaspBee II](https://phoscon.de/raspbee2) Zigbee shields for Raspberry Pi
* [ConBee](https://phoscon.de/conbee) and [ConBee II](https://phoscon.de/conbee2) USB radio stick for PC and Raspberry Pi

## Features
- Support for Zigbee Home Automation (HA) and Zigbee Light Link (ZLL) based lights
- Add, remove and modify groups of lights
- Control single lights or groups
- Control colors and dimmlevels via hue, saturation, brightness, CIE xy color coordinates
- Smooth transitions of colors and dimming over time
- Save and recall individual scenes for a group
- Create rules to automate light control
- Trigger timed commands
- Reset ZLL lights to factory new state

## Extensibility
The [deCONZ REST-API Plugin](https://github.com/dresden-elektronik/deconz-rest-plugin) is a Open Source project licensed under the BSD license and available at GitHub. It could therefore be extended with further functionality, for example to support more devices.
