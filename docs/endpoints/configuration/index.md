---
title: Configuration
---

# Configuration

This endpoint allows to retreive and modify the current configuration of the gateway.


## Acquire API key<a name="aquireapikey">&nbsp;</a>

    POST /api

Creates a new [API key](../../misc/authorization) which provides authorized access to the REST-API.

!!! note
    The request will only succeed if the gateway is unlocked or valid HTTP basic authentification credentials are provided in the HTTP request header see [authorization](../../misc/authorization).

### Parameters

<table class="table table-bordered">
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>devicetype</td>
            <td>String (0&ndash;40 chars)</td>
            <td>Name of the client application.</td>
            <td>required</td>
        </tr>
        <tr>
            <td>username</td>
            <td>String (10&ndash;40 chars)</td>
            <td>Will be used as username. If not specified a random key will be generated.</td>
            <td>optional</td>
        </tr>
    </tbody>
</table>

### Example request data
    {
        "username": "988112a4e198cc1211",
        "devicetype": "my application"
    }

### Response

<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "username": "988112a4e198cc1211" } } ]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors)

[403 Forbidden](../../misc/errors)

------------------------------------------------------

## Delete API key<a name="deleteapikey">&nbsp;</a>

    DELETE /api/<apikey>/config/whitelist/<apikey2>

Deletes an API key so it can no longer be used.

### Parameters

None

### Possible errors

[403 Forbidden](../../misc/errors)

[404 Not Found](../../misc/errors)

------------------------------------------------------

## Get configuration<a name="getconfig">&nbsp;</a>

    GET /api/<apikey>/config

Returns the current gateway configuration.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "203941fel3ds8ad61903224"
</code>
</pre>
<pre class="highlight">
<code>
{
    "apiversion": "1.16.0",
    "bridgeid": "00212EFFFF00C5FB",
    "devicename": "ConBee II",
    "dhcp": true,
    "fwversion": "0x26660700",
    "gateway": "192.168.80.1",
    "ipaddress": "192.168.80.142",
    "linkbutton": false,
    "localtime": "2020-06-29T14:00:40",
    "mac": "74:46:a0:9e:92:c7",
    "modelid": "deCONZ",
    "name": "deCONZ-GW",
    "netmask": "255.255.255.0",
    "networkopenduration": 60,
    "ntp": "synced",
    "panid": 56889,
    "portalservices": false,
    "proxyaddress": "",
    "proxyport": 0,
    "rfconnected": true,
    "swupdate": {
        "notify": false,
        "text": "",
        "updatestate": 0,
        "url": "",
    },
    "swversion": "2.6.0",
    "timeformat": "12h",
    "timezone": "Europe/Berlin",
    "UTC": "2020-06-29T12:00:40",
    "uuid": "a65d80a1-975a-4598-8d5a-2547bc18d63b",
    "websocketnotifyall": true,
    "websocketport": 23765,
    "whitelist": {},
    "zigbeechannel": 20
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
            <td>apiversion</td>
            <td>String</td>
            <td>The version of the deCONZ Rest API</td>
        </tr>
        <tr>
            <td>bridgeid</td>
            <td>String</td>
            <td>The unique identifier for the gateway.</td>
        </tr>
        <tr>
            <td>devicename</td>
            <td>String</td>
            <td>The product name of the gateway. Valid values are "ConBee", "RaspBee", "ConBee II" and "RaspBee II".</td>
        </tr>
        <tr>
            <td>dhcp</td>
            <td>Bool</td>
            <td>Whether the IP address of the bridge is obtained with DHCP.</td>
        </tr>
        <tr>
            <td>fwversion</td>
            <td>String</td>
            <td>The current Zigbee firmware version.</td>
        </tr>
        <tr>
            <td>gateway</td>
            <td>String</td>
            <td>IPv4 address of the gateway.</td>
        </tr>
        <tr>
            <td>ipaddress</td>
            <td>String</td>
            <td>IPv4 address of the gateway.</td>
        </tr>
         <tr>
            <td>linkbutton</td>
            <td>Bool</td>
            <td>true if the gateway is unlocked.</td>
        </tr>
         <tr>
            <td>localtime</td>
            <td>String</td>
            <td>The localtime of the gateway</td>
        </tr>
        <tr>
            <td>mac</td>
            <td>String</td>
            <td>MAC address of the gateway.</td>
        </tr>
        <tr>
            <td>modelid</td>
            <td>String</td>
            <td>Fixed string "deCONZ".</td>
        </tr>
        <tr>
            <td>name</td>
            <td>String</td>
            <td>Name of the gateway.</td>
        </tr>
        <tr>
            <td>netmask</td>
            <td>String</td>
            <td>Network mask of the gateway.</td>
        </tr>
        <tr>
            <td>networkopenduration</td>
            <td>Number (1&ndash;65535)</td>
            <td>The duration in seconds used by lights and sensors search, see <a href="#modifyconfiguration">Modify configuration</a>.</td>
        </tr>
        <tr>
            <td>ntp</td>
            <td>String</td>
            <td>Only for gateways running on Linux. Tells if the NTP time is "synced" or "unsynced".</td>
        </tr>
        <tr>
            <td>panid</td>
            <td>Number (0&ndash;65535)</td>
            <td>The Zigbee pan ID of the gateway.</td>
        </tr>
        <tr>
            <td>portalservices</td>
            <td>Bool</td>
            <td>This indicates whether the bridge is registered to synchronize data with a portal account.</td>
        </tr>
        <tr>
            <td>proxyaddress</td>
            <td>String</td>
            <td>Not supported</td>
        </tr>
        <tr>
            <td>proxyport</td>
            <td>Number</td>
            <td>Not supported</td>
        </tr>
        <tr>
            <td>rfconnected</td>
            <td>Bool</td>
            <td>Is true when the deCONZ is connected with the firmware and the Zigbee network is up.</td>
        </tr>
        <tr>
            <td>softwareupdate</td>
            <td>Object</td>
            <td>Contains information related to software updates.</td>
        </tr>
        <tr>
            <td>swversion</td>
            <td>String</td>
            <td>The software version of the gateway.</td>
        </tr>
        <tr>
            <td>timeformat</td>
            <td>String</td>
            <td>Stores a value of the timeformat that can be used by other applications. "12h" or "24h"</td>
        </tr>
        <tr>
            <td>timezone</td>
            <td>String</td>
            <td>Timezone used by the gateway (only on Raspberry Pi). "None" if not further specified.</td>
        </tr>
        <tr>
            <td>UTC</td>
            <td>String</td>
            <td>Current UTC time of the gateway in ISO 8601 format.</td>
        </tr>
        <tr>
            <td>uuid</td>
            <td>String</td>
            <td>UPNP Unique Id of the gateway</td>
        </tr>
        <tr>
            <td>websocketnotifyall</td>
            <td>Bool</td>
            <td>When true all state changes will be signalled through the Websocket connection (default true).</td>
        </tr>
        <tr>
            <td>websocketport</td>
            <td>Number</td>
            <td>Port of the Websocket server.</td>
        </tr>
        <tr>
            <td>whitelist</td>
            <td>Object</td>
            <td>An array of whitelisted API keys.</td>
        </tr>
        <tr>
            <td>zigbeechannel</td>
            <td>Number</td>
            <td>The current wireless frequency channel used by the Gateway. Supported channels: 11, 15, 20, 25.</td>
        </tr>
    </tbody>
</table>

### Possible errors

[304 Not Modified](../../misc/errors)

[403 Forbidden](../../misc/errors)

------------------------------------------------------

## Get full state<a name="getfullstate">&nbsp;</a>

    GET /api/<apikey>

Returns the full state of the gateway including all its lights, groups, scenes and schedules.

### Parameters

None

### Response

<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "203941fel3ds8ad61903224"
</code>
</pre>
<pre class="highlight">
<code>
{
    "config": {
        "dhcp": true,
        "gateway": "192.168.178.1",
        "ipaddress": "192.168.192.237",
        "linkbutton": true,
        "mac": "E0:69:95:58:06:7F",
        "name": "RaspBee GW",
        "netmask": "255.255.255.0",
        "portalservices": false,
        "proxyaddress": "",
        "proxyport": 0,
        "swupdate": {
            "notify": false,
            "text": "",
            "updatestate": 0,
            "url": ""
        },
        "swversion": "1.12.3",
        "utc": "2013-05-22T12:02:30",
        "whitelist": {}
    },
    "groups": {
        "1": {
            "action": {
                "bri": 3945,
                "colormode": "hs",
                "ct": 500,
                "effect": "none",
                "hue": 0,
                "on": true,
                "sat": 17680,
                "xy": [0.0610457, 0.219979]
            },
            "devicemembership": [],
            "etag": "893f60b611274d1803207298cf26b1e1",
            "hidden": false,
            "lights": [ "1" ],
            "lightsequence": [ "1" ],
            "multideviceids": [],
            "name": "Office",
            "scenes": [ 
                "0": {
                    "id": "1",
                    "name": "blue moon"
                }
           ]
        }
    },
    "lights": {
        "1": {
            "etag": "030cf8c1c0025420f3a0659afab251f5",
            "name": "Desk Lamp",
            "modelid": "FLS-PP-01",
            "pointsymbol": {},
            "swversion": "14010400",
            "type": "Color Dimmable Light",
            "state": {
                "on": true,
                "bri": 190,
                "hue": 21672,
                "sat": 254,
                "ct": 500,
                "alert": "none",
                "colormode": "hs",
                "effect": "none",
                "reachable": true,
                "xy": [ 0.805343, 0.000612754 ]
            }
        }
    },
    "schedules": {
        "1": {
            "autodelete": false
            "command": {
            "address": "/api/AD4F14F244/groups/2/scenes/1/recall"
            "body": {}
            "method": "PUT"
            }
            "etag": "3dea322b33d34a9134e5632706448f8f"
            "name": "Good Morning"
            "status": "enabled"
            "time": "W124/T05:00:00"
        }
    },
    "sensors": {
        1: {
            "config": {
                "on": true
                "reachable": false
            }
            "etag": "01252de8b14f62a234a4680827cf1609"
            "manufacturername": "dresden elektronik"
            "mode": 2
            "modelid": "Lighting Switch"
            "name": "Lighting Switch 1"
            "state": {
                "lastupdated": "2016-06-29T13:16:41"
            }
            "swversion": "1.0"
            "type": "ZHASwitch"
            "uniqueid": "0x00212effff00a6bc"
            }
        }
	"rules": {}
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
            <td>config</td>
            <td>Object</td>
            <td>Configuration of the gateway.</td>
        </tr>
        <tr>
            <td>groups</td>
            <td>Object</td>
            <td>All groups of the gateway.</td>
        </tr>
        <tr>
            <td>lights</td>
            <td>Object</td>
            <td>All lights of the gateway.</td>
        </tr>
		 <tr>
            <td>rules (as from deconz version > 2.04.12)</td>
            <td>Object</td>
            <td>All rules of the gateway.</td>
        </tr>
        <tr>
            <td>schedules</td>
            <td>Object</td>
            <td>All schedules of the gateway.</td>
        </tr>
    </tbody>
</table>

### Possible errors

[304 Not Modified](../../misc/errors)

[403 Forbidden](../../misc/errors)

------------------------------------------------------

## Modify configuration<a name="modifyconfiguration">&nbsp;</a>

    PUT /api/<apikey>/config

Modify configuration parameters.

### Parameters

<table class="table table-bordered">
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>name</td>
            <td>String (0&ndash;16 chars)</td>
            <td>Name of the gateway.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>rfconnected</td>
            <td>Bool</td>
            <td>Set connected state of the gateway.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>updatechannel</td>
            <td>String</td>
            <td>Set update channel ("stable"|"alpha"|"beta").</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>permitjoin</td>
            <td>Number (0&ndash;255)</td>
            <td>Open the network so that other zigbee devices can join. 0 = network closed, 255 = network open, 1&ndash;254 = time in seconds the network remains open. The value will decrement automatically.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>groupdelay</td>
            <td>Number (0&ndash;5000)</td>
            <td>Time between two group commands in milliseconds.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>otauactive</td>
            <td>Bool</td>
            <td>Set OTAU active or inactive.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>discovery</td>
            <td>Bool</td>
            <td>Set gateway discovery over the internet active or inactive.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>networkopenduration</td>
            <td>Number (1&ndash;65535)</td>
            <td>Sets the lights and sensors search duration in seconds.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>rfconnected</td>
            <td>Bool</td>
            <td>Set to true to bring the Zigbee network up and false to bring it down. This has the same effect as using the Join and Leave buttons in deCONZ.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>unlock</td>
            <td>Number (0&ndash;600)</td>
            <td>Unlock the gateway so that apps can register themselves to the gateway (time in seconds).</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>zigbeechannel</td>
            <td>Number (11|15|20|25)</td>
            <td>Set the zigbeechannel of the gateway. Notify other Zigbee devices also to change their channel.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>timezone</td>
            <td>String</td>
            <td>Set the timezone of the gateway (only on Raspberry Pi).
                Format: tzdatabase e.g. “Europe/Berlin”
                <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">Wikipedia:ListOfTimeZones</a></td>
            <td>optional</td>
        </tr>
        <tr>
            <td>utc</td>
            <td>String</td>
            <td>Set the UTC time of the gateway (only on Raspbery Pi) in ISO 8601 format (yyyy-MM-ddTHH:mm:ss).</td>
            <td>optional</td>
        </tr>
		<tr>
            <td>timeformat</td>
            <td>String</td>
            <td>Can be used to store the timeformat permanently. It can be either "12h" or "24h".</td>
            <td>optional</td>
        </tr>
    </tbody>
</table>

### Example request data

<pre class="headers">
<code>
{
  "zigbeechannel": 25
}
</code>
</pre>

### Response

<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "203941fel3ds8ad61903224"
</code>
</pre>
<pre class="highlight">
<code>
[
  { 
    "success": {"/config/zigbeechannel": 25 }
  }
]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors)

------------------------------------------------------

## Update software<a name="updatesoftware">&nbsp;</a>

    POST /api/<apikey>/config/update

Returns the newest software version available. Starts the update if available (only on Raspberry Pi).

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
    "/config/update": "2.04.05"
  }
}
</code>
</pre>

------------------------------------------------------

## Update firmware<a name="updatefirmware">&nbsp;</a>

    POST /api/<apikey>/config/updatefirmware

Starts the update firmware process if newer version is available.

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
    "/config/updatefirmware": "26050500"
  }
}
</code>
</pre>

### Possible errors

[503 Service Unavailable](../../misc/errors)

<!--

## Export gateway configuration<a name="export">&nbsp;</a>

    POST /api/<apikey>/config/export

Exports the current gateway network settings and database. An archive with the name deCONZ.tar.gz will be created in the deCONZ data directory. It can be downloaded via the hyperlink http://\<gateway_ip>/deCONZ.tar.gz

When downloaded the file will be renamed to raspbee_gateway_config_yyyy-MM-dd.dat

### Response

<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
{
  "success": { 
    "/config/export": "success"
  }
}
</code>
</pre>

### Possible errors

[503 Service Unavailable](../../misc/errors)

------------------------------------------------------

## Import gateway configuration<a name="import">&nbsp;</a>

    POST /api/<apikey>/config/import

Imports a raspbee_gateway_config_yyyy-MM-dd.dat file and apply the stored settings. The file can be renamed but must keep the ending .dat. The file must be uploaded to the gateway beforehand.

For fileupload you can use
    
    POST /api/fileupload 

### Response

<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
{
  "success": { 
    "/config/import": "success"
  }
}
</code>
</pre>

### Possible errors

[503 Service Unavailable](../../misc/errors)

-->

------------------------------------------------------

## Reset gateway<a name="reset">&nbsp;</a>

    POST /api/<apikey>/config/reset

Reset the gateway network settings to factory new and/or delete the deCONZ database (config, lights, scenes, groups, schedules, devices, rules).

### Parameters

<table class="table table-bordered">
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>resetGW</td>
            <td>Bool</td>
            <td>Set the network settings of the gateway to factory new.</td>
            <td>optional</td>
        </tr>
        <tr>
            <td>deleteDB</td>
            <td>Bool</td>
            <td>Delete the Database.</td>
            <td>optional</td>
        </tr>
    </tbody>
</table>

At least one parameter is required!

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
    "/config/reset": "success"
  }
}
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors)

[503 Service Unavailable](../../misc/errors)

------------------------------------------------------

## Change password<a name="changepw">&nbsp;</a>

    PUT /api/<apikey>/config/password

Change the Password of the Gateway. The parameter must be a Base64 encoded string of `<username>:<password>`.

### Parameters

<table class="table table-bordered">
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>username</td>
            <td>String</td>
            <td>The user name (currently only “delight” is supported).</td>
            <td>required</td>
        </tr>
        <tr>
            <td>oldhash</td>
            <td>String</td>
            <td>The Base64 encoded combination of “username:old password”.</td>
            <td>required</td>
        </tr>
        <tr>
            <td>newhash</td>
            <td>String</td>
            <td>The Base64 encoded combination of “username:new password”.</td>
            <td>required</td>
        </tr>
    </tbody>
</table>

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
    "/config/password": "changed"
  }
}
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors)

[401 Unauthorized](../../misc/errors)

------------------------------------------------------

## Reset password<a name="resetpw">&nbsp;</a>

    DELETE /api/<apikey>/config/password

Resets the username and password to default username = “delight” and password = "delight”. The request can only succeed within 10 minutes after gateway start.

### Response

<pre class="headers">
  <code class="no-highlight">
    HTTP/1.1 200 OK
  </code>
</pre>
<pre class="highlight">
  <code>
    {}
  </code>
</pre>

### Possible errors

[403 Forbidden](../../misc/errors)
