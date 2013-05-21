---
layout: page
title: deCONZ REST API
tagline: Documentation
---
{% include JB/setup %}

{% include sitepanelnav %}

## Introduction

This documentation describes the deCONZ REST API, which is provided by the [deCONZ REST Plugin](#) that runs a lightweight HTTP server within the [deCONZ](http://www.dresden-elektronik.de/funktechnik/products/software/pc/deconz) application.

The REST API allows third party applications easy monitoring and control of a ZigBee network from local or remote operating clients.

## Features
For now the API provides follwoing capabilities:

- Support for ZigBee Home Automation (HA) and ZigBee Light Link (ZLL) based lights
- Add, remove and modify groups of lights
- Control single lights or groups
- Control colors and dimmlevel of lights (hue, saturation, brightness, CIE xyY, color temperature)
- Smooth dimming
- Add, remove and modify light scenes of a group

## Extensibility
The [deCONZ REST Plugin](#) is a open source project available at GitHub and could therefore extended with further functionality, for example to support more devices.
