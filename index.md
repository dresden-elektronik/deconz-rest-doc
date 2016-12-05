---
layout: page
title: deCONZ REST API
tagline: Documentation
---
{% include JB/setup %}

## Introduction

This documentation describes the REST API, which is provided by the [deCONZ REST API Plugin](http://github.com/dresden-elektronik/deconz-rest-plugin) from [dresden elektronik](http://www.dresden-elektronik.de?L=1) that runs a lightweight HTTP server within the [deCONZ](http://www.dresden-elektronik.de/funktechnik/products/software/pc/deconz?L=1) application on the Raspberry Pi.

The REST API allows third party applications easy monitoring and control of a ZigBee network from local or remote operating clients.

One of the following devices is needed to get ZigBee support on the Raspberry Pi or PC.

* [RaspBee](http://www.dresden-elektronik.de/funktechnik/solutions/wireless-light-control/raspbee?L=1) ZigBee shield for Raspberry Pi
* [ConBee](https://www.dresden-elektronik.de/funktechnik/solutions/wireless-light-control/conbee/?L=1) USB radio stick for PC or Raspberry Pi

## Features
- Support for ZigBee Home Automation (HA) and ZigBee Light Link (ZLL) based lights
- Add, remove and modify groups of lights
- Control single lights or groups
- Control colors and dimmlevels via hue, saturation, brightness, CIE xy color coordinates
- Smooth transitions of colors and dimming over time
- Save and recall individual scenes for a group
- Create rules to automate light control
- Trigger timed commands
- Reset ZLL lights to factory new state

## Extensibility
The [deCONZ REST API Plugin](http://github.com/dresden-elektronik/deconz-rest-plugin) is a open source project licensed under the BSD license and available at GitHub. It could therefore be extended with further functionality, for example to support more devices.
