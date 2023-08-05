---
title: Devices
---

# Devices

The Devices endpoint can be used to obtain more details on a device and its capabilities. It is also used to pair devices by using zigbee install codes.

## Get all Devices<a name="getall">&nbsp;</a>

    GET /api/<apikey>/devices

Returns a list of all devices. If there are no devices in the system, an empty object {} is returned.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[
  "00:21:2e:ff:ff:47:62:36",
  "00:15:8d:00:a3:b4:00:f2",
  "00:15:8d:00:13:b9:29:e7"
]
</code>
</pre>

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get Device<a name="getdevice">&nbsp;</a>

    GET /api/<apikey>/devices/<device_mac_address>

Returns the device details with the specified device MAC address.

!!! Important
    The device MAC address in the request URL must be provided with colons!

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
{
  "lastannounced": null,
  "lastseen": "2023-08-05T20:04Z",
  "manufacturername": "IKEA of Sweden",
  "modelid": "TRADFRI remote control",
  "name": "TRADFRI remote control",
  "productid": "TRADFRI remote control E1810",
  "subdevices": [
    {
      "config": {
        "alert": {
          "lastupdated": "2022-09-24T22:57:55Z",
          "value": "none"
        },
        "battery": {
          "lastupdated": "2023-03-10T00:47:58Z",
          "value": 0
        },
        "group": {
          "lastupdated": "2022-09-24T22:57:55Z",
          "value": "8"
        },
        "on": {
          "lastupdated": "2022-09-24T22:59:55Z",
          "value": true
        },
        "reachable": {
          "lastupdated": "2023-08-05T22:09:43Z",
          "value": true
        }
      },
      "state": {
        "buttonevent": {
          "lastupdated": "2022-09-24T23:03:58Z",
          "value": 1002
        }
      },
      "type": "ZHASwitch",
      "uniqueid": "60:a4:23:ff:ba:f0:47:22-01-1000"
    }
  ],
  "swversion": "2.3.014",
  "uniqueid": "60:a4:23:ff:ba:f0:47:22"
}
</code>
</pre>

#### Response fields

!!! Todo
    General device information, config and state attributes of the defined subdevices with
    their respective values including last update time are presented.

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Pair with install code<a name="installcode">&nbsp;</a>

    PUT /api/<apikey>/devices/<device_mac_address>/installcode

Pair a device by using zigbee install code.

!!! Important
    The device MAC address in the request URL must be provided without colons!

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>installcode</td>
      <td>String</td>
      <td>
        <p>6, 8, 12 or 16 Byte device installation code, plus 2 Byte CRC.</p>
        <p>This is an example of a 16 Byte code + 2 Byte CRC: 83FE D340 7A93 9723 A5C6 39B2 6916 D505 C3B5</p>
      </td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data

    {
      "installcode": "83FED3407A939723A5C639B26916D505C3B5"
    }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
    {
      "success": {
        "installcode": "83FED3407A939723A5C639B26916D505C3B5",
        "mmohash": "66B6900981E1EE3CA4206B6B861C02BB"
      }
    }
</code>
</pre>

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>installcode</td>
      <td>String</td>
      <td>The device install code provided in the request.</td>
    </tr>
    <tr>
      <td>mmohash</td>
      <td>String</td>
      <td>
        <p>The Matyas-Meyer-Oseas (MMO) hash calculated based on the provided installation code.</p>
        <p>It is automatically used by deCONZ to enable pairing with the target device.</p>
      </td>
    </tr>
  </tbody>
</table>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

