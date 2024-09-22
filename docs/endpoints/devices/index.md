---
title: Devices
---

# Devices

The Devices endpoint can be used to obtain more details on a device and its capabilities. It is also used to pair devices by using zigbee install codes.

## Get all Devices<a name="getall">&nbsp;</a>

    GET /api/<apikey>/devices

Returns a list of all devices. If there are no devices in the system, an empty array [] is returned.

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
  "ddf_hash": "042fa35e2038292f639a9eb24910b702b514c6680adc10aedf00f4644ecf7515",
  "ddf_policy": "latest_prefer_stable",
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

## Get Device DDF<a name="getdeviceddf">&nbsp;</a>

    GET /api/<apikey>/devices/<device_mac_address>/ddf

Returns the DDF of the device specified by the provided MAC address.

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
  "schema": "devcap1.schema.json",
  "manufacturername": "$MF_IKEA",
  "modelid": "TRADFRI remote control",
  "vendor": "IKEA of Sweden",
  "product": "TRADFRI remote control E1810",
  "sleeper": true,
  "status": "Gold",
  "path": "/devices/ikea.json",
  "subdevices": [
    {
      "type": "$TYPE_SWITCH",
      "restapi": "/sensors",
      "uuid": [
        "$address.ext",
        "0x01",
        "0x1000"
      ],
      "meta": {
        "group.endpoints": [
          1
        ]
      },
      "fingerprint": {
        "profile": "0x0104",
        "device": "0x0820",
        "endpoint": "0x01",
        "in": [
          "0x0000",
          "0x0001",
          "0x1000"
        ],
        "out": [
          "0x0006",
          "0x0008",
          "0x0005"
        ]
      },
      "items": [
        {
          "name": "attr/id"
        },
        {
          "name": "attr/lastannounced"
        },
        {
          "name": "attr/lastseen"
        },
        {
          "name": "attr/manufacturername"
        },
        {
          "name": "attr/modelid"
        },
        {
          "name": "attr/name"
        },
        {
          "name": "attr/swversion"
        },
        {
          "name": "attr/type"
        },
        {
          "name": "attr/uniqueid"
        },
        {
          "name": "config/alert"
        },
        {
          "name": "config/battery",
          "refresh.interval": 86400,
          "read": {
            "at": "0x0021",
            "cl": "0x0001",
            "ep": 1,
            "fn": "zcl"
          },
          "parse": {
            "at": "0x0021",
            "cl": "0x0001",
            "ep": 1,
            "eval": "Item.val = Attr.val;",
            "fn": "zcl"
          },
          "default": 0
        },
        {
          "name": "config/group",
          "default": "auto"
        },
        {
          "name": "config/on"
        },
        {
          "name": "config/reachable"
        },
        {
          "name": "state/buttonevent",
          "awake": true
        },
        {
          "name": "state/lastupdated"
        }
      ]
    }
  ],
  "bindings": [
    {
      "bind": "unicast",
      "src.ep": 1,
      "cl": "0x0001",
      "report": [
        {
          "at": "0x0021",
          "dt": "0x20",
          "min": 300,
          "max": 3600,
          "change": "0x00000001"
        }
      ]
    },
    {
      "bind": "groupcast",
      "config.group": 0,
      "src.ep": 1,
      "cl": "0x0005"
    },
    {
      "bind": "groupcast",
      "config.group": 0,
      "src.ep": 1,
      "cl": "0x0006"
    },
    {
      "bind": "groupcast",
      "config.group": 0,
      "src.ep": 1,
      "cl": "0x0008"
    }
  ]
}
</code>
</pre>

#### Response fields

!!! Note
    The device returns the full DDF for the device.

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Get Full Device DDF<a name="getdeviceddffull">&nbsp;</a>

    GET /api/<apikey>/devices/<device_mac_address>/ddffull

Returns the full DDF of the device specified by the provided MAC address.

!!! Important
    The device MAC address in the request URL must be provided with colons!
    
!!! Note
    There's currently no real distinction between DDF and full DDF (yet).

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
  "schema": "devcap1.schema.json",
  "manufacturername": "$MF_IKEA",
  "modelid": "TRADFRI remote control",
  "vendor": "IKEA of Sweden",
  "product": "TRADFRI remote control E1810",
  "sleeper": true,
  "status": "Gold",
  "path": "/devices/ikea.json",
  "subdevices": [
    {
      "type": "$TYPE_SWITCH",
      "restapi": "/sensors",
      "uuid": [
        "$address.ext",
        "0x01",
        "0x1000"
      ],
      "meta": {
        "group.endpoints": [
          1
        ]
      },
      "fingerprint": {
        "profile": "0x0104",
        "device": "0x0820",
        "endpoint": "0x01",
        "in": [
          "0x0000",
          "0x0001",
          "0x1000"
        ],
        "out": [
          "0x0006",
          "0x0008",
          "0x0005"
        ]
      },
      "items": [
        {
          "name": "attr/id"
        },
        {
          "name": "attr/lastannounced"
        },
        {
          "name": "attr/lastseen"
        },
        {
          "name": "attr/manufacturername"
        },
        {
          "name": "attr/modelid"
        },
        {
          "name": "attr/name"
        },
        {
          "name": "attr/swversion",
          "refresh.interval": 86400,
          "read": {
            "at": "0x4000",
            "cl": "0x0000",
            "ep": 0,
            "fn": "zcl"
          },
          "parse": {
            "at": "0x4000",
            "cl": "0x0000",
            "ep": 255,
            "eval": "Item.val = Attr.val",
            "fn": "zcl"
          }
        },
        {
          "name": "attr/type"
        },
        {
          "name": "attr/uniqueid"
        },
        {
          "name": "config/alert"
        },
        {
          "name": "config/battery",
          "refresh.interval": 86400,
          "read": {
            "at": "0x0021",
            "cl": "0x0001",
            "ep": 1,
            "fn": "zcl"
          },
          "parse": {
            "at": "0x0021",
            "cl": "0x0001",
            "ep": 1,
            "eval": "Item.val = Attr.val;",
            "fn": "zcl"
          },
          "default": 0
        },
        {
          "name": "config/group",
          "default": "auto"
        },
        {
          "name": "config/on",
          "default": true
        },
        {
          "name": "config/reachable"
        },
        {
          "name": "state/buttonevent",
          "awake": true
        },
        {
          "name": "state/lastupdated"
        }
      ]
    }
  ],
  "bindings": [
    {
      "bind": "unicast",
      "src.ep": 1,
      "cl": "0x0001",
      "report": [
        {
          "at": "0x0021",
          "dt": "0x20",
          "min": 300,
          "max": 3600,
          "change": "0x00000001"
        }
      ]
    },
    {
      "bind": "groupcast",
      "config.group": 0,
      "src.ep": 1,
      "cl": "0x0005"
    },
    {
      "bind": "groupcast",
      "config.group": 0,
      "src.ep": 1,
      "cl": "0x0006"
    },
    {
      "bind": "groupcast",
      "config.group": 0,
      "src.ep": 1,
      "cl": "0x0008"
    }
  ]
}
</code>
</pre>

#### Response fields

!!! Note
    The device returns the full DDF for the device.

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Reload Device DDF<a name="reloadddf">&nbsp;</a>

    PUT /api/<apikey>/devices/<device_mac_address>/ddf/reload

Reload the DDF for the specified device MAC address. This might be required if you made some changes.

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
[ { "success": { "reload": "60:a4:23:ff:ba:f0:47:22" } } ]
</code>
</pre>

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>reload</td>
      <td>String</td>
      <td>The MAC address for which the DDF has been reloaded.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Get Device Resource Item Introspection<a name="itemintrospection">&nbsp;</a>

    GET /api/<apikey>/devices/<uniqueid>/<prefix>/<item>/introspect

Get the data type of the respective resource item as well as its defined values/boundaries or other relevant data.

!!! Note
    Prefix encompasses `config`, `state` and `attr`.
    Item resents the typical and known resource items.

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
  "maxval": 100,
  "minval": 0,
  "type": "uint8"
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
      <td>maxval</td>
      <td>Number</td>
      <td>The defined maximum numeric value.</td>
    </tr>
    <tr>
      <td>maxval</td>
      <td>Number</td>
      <td>The defined minimum numeric value.</td>
    </tr>
    <tr>
      <td>type</td>
      <td>String</td>
      <td>The defined data type of the resource item.</td>
    </tr>
    <tr>
      <td>buttons</td>
      <td>Object</td>
      <td>Contains the button and the respective function.</td>
    </tr>
    <tr>
      <td>values</td>
      <td>Object</td>
      <td>Contains e.g. the `buttonevent` value, a short description and the generating button.</td>
    </tr>
  </tbody>
</table>

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

------------------------------------------------------

## Set DDF policy<a name="put_ddf_policy">&nbsp;</a>

    PUT /api/<apikey>/devices/<device_mac_address>/ddf/policy

`since v2.27.0-beta`

Sets the device DDF policy and optional bundle hash to be pinned. The policy determines which DDF bundle is loaded for a device, like a stable or beta signed, un-signed or specific bundle (pinned).

By executing this request the matching DDF bundle will be hot-reloaded for the device. This allows switching to a different bundle at runtime.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>policy</td>
      <td>String</td>
      <td>
        <p>latest_prefer_stable</p>
        <p>latest</p>
        <p>pin</p>
        <p>raw_json</p>
      </td>
      <td>required</td>
    </tr>
    <tr>
      <td>hash</td>
      <td>String</td>
      <td>
        <p>DDF bundle hash (64 characters)</p>
        <p>Required if policy is <b>pin</b>.</p>
      </td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

Policy               | Description
---------------------|--------------------------------
latest_prefer_stable | **(default)** Use latest DDF bundle: beta signed one if no stable available.
latest               | Use latest DDF bundle either beta or stable signed or un-signed as fallback.
pin                  | Use and stay on bundle given by `<hash>`.
raw_json             | For development like before bundles existed just use raw .json DDF files.

### Example request data
    {
      "policy": "pin",
      "hash": "042fa35e2038292f639a9eb24910b702b514c6680adc10aedf00f4644ecf7515"
    }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[
  {
    "success": {
      "/devices/00:17:88:01:02:00:21:f4/ddf/policy": "pin"
    }
  },
  {
    "success": {
      "/devices/00:17:88:01:02:00:21:f4/ddf/hash": "042fa35e2038292f639a9eb24910b702b514c6680adc10aedf00f4644ecf7515"
    }
  }
]
</code>
</pre>

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>policy</td>
      <td>String</td>
      <td>The DDF policy provided in the request.</td>
    </tr>
    <tr>
      <td>hash</td>
      <td>String</td>
      <td>
        <p>The DDF bundle hash provided in the request.</p>
        <p>(Only present for the <b>pin</b> policy)</p>
      </td>
    </tr>
  </tbody>
</table>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)