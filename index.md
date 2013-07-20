---
layout: page
title: deCONZ REST API
tagline: Documentation
---
{% include JB/setup %}

## Introduction

This documentation describes the REST API, which is provided by the [deCONZ REST API Plugin](http://github.com/dresden-elektronik/deconz-rest-plugin) from [dresden elektronik](http://www.dresden-elektronik.de?L=1) that runs a lightweight HTTP server within the [deCONZ](http://www.dresden-elektronik.de/funktechnik/products/software/pc/deconz?L=1) application.

The REST API allows third party applications easy monitoring and control of a ZigBee network from local or remote operating clients.

## Features
For now the API provides following capabilities:

- Support for ZigBee Home Automation (HA) and ZigBee Light Link (ZLL) based lights
- Add, remove and modify groups of lights
- Control single lights or groups
- Control colors and dimmlevels via hue, saturation, brightness, CIE xy color coordinates and color temperature
- Smooth transitions of colors and dimming over time
- Save and recall individual scenes for a group
- Trigger timed commands

## Extensibility
The [deCONZ REST API Plugin](http://github.com/dresden-elektronik/deconz-rest-plugin) is a open source project licensed under the BSD license and available at GitHub. It could therefore be extended with further functionality, for example to support more devices.
