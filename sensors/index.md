---
layout: page
title: Sensors
nav: endpoints
order: 7
anchors:
  - title: Create sensor
    url: "#create"
  - title: Get all sensors
    url: "#getall"
  - title: Get sensor
    url: "#getsensor"
  - title: Updated sensor
    url: "#update"
  - title: Change sensor config
    url: "#changeconfig"
  - title: Change sensor state
    url: "#changestate"
  - title: Delete sensor
    url: "#delete"

---

{% include JB/setup %}

Sensors can be used to measure environment parameters like brightness or activation of a switch. With a coressponding rule they can control lights and groups.

## Create sensor<a name="create">&nbsp;</a>

    POST /api/<apikey>/sensors

Creates a new sensor.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the sensor.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>String</td>
      <td>The model identifier of the sensor.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>swversion</td>
      <td>String</td>
      <td>The software version of the sensor.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>type</td>
      <td>String</td>
      <td>The type of the sensor (see: allowed sensor types and its states).</td>
      <td>required</td>
    </tr>
    <tr>
      <td>uniqueid</td>
      <td>String</td>
      <td>The unique id of the sensor. Should be the MAC address of the device.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>String</td>
      <td>The manufacturer name of the sensor.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Object</td>
      <td>The state of the sensor (see: supported sensor types and its states).</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>config</td>
      <td>Object</td>
      <td>The config of the sensor.
        <ul>
          <li>on - Bool - default: true</li>
          <li>reachable - Bool - default: true</li>
          <li>battery - Number (0..100)</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Supported sensor types and its states

<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>Supported state</th><th>Type</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>ZHASwitch</td>
      <td>buttonevent</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHALight</td>
      <td>lux</td>
      <td>Number</td>
    </tr>
     <tr>
      <td>ZHAPresence</td>
      <td>presence</td>
      <td>Bool</td>
    </tr>
  </tbody>
</table>

### Example request data

<pre class="highlight">
<code>    
{
    "config": {
        "on": true
        "reachable": true
    }
    "manufacturername": "Me"
    "modelid": "T1000"
    "name": "My Switch"
    "swversion": "1.0"
    "type": "CLIPSwitch"
    "uniqueid": "0x001fee00000008bb"
}
</code>
</pre>

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "1" } } ];
</code>
</pre>

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>String</td>
      <td>The unique identifier of the new sensor.</td>
    </tr>
  </tbody>
</table>


### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get all Sensors<a name="getall">&nbsp;</a>

    GET /api/<apikey>/sensors

Returns a list of all Sensors. If there are no sensors in the system then an empty object {} will be returned.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
{
    "1": {
        "config": {
            "on": true,
            "reachable": true
        },
        "ep": 1,
        "etag": "61eaee2477fc3d5c27932fefeef638bd",
        "manufacturername": "dresden elektronik",
        "modelid": "Lighting Switch",
        "name": "Lighting Switch 1",
        "state": {
            "lastupdated": "2016-07-06T09:39:53"
        },
        "swversion": "1.0",
        "type": "ZHASwitch",
        "uniqueid": "0x00212effff00a6bc"
    }
    "2": {
        "config": {
            "on": true,
            "reachable": true
        },
        "ep": 2,
        "etag": "61eaee2477fc3d5c27932fefeef638bd",
        "manufacturername": "dresden elektronik",
        "modelid": "Lighting Switch",
        "name": "Lighting Switch 2",
        "state": {
            "lastupdated": "2016-07-06T09:39:53"
        },
        "swversion": "1.0",
        "type": "ZHASwitch",
        "uniqueid": "0x00212effff00a6bc"
    }
}
</code>
</pre>

#### Response fields

The whole sensor object as descripted in [Get sensor](#getsensor).

### Possible errors

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get sensor<a name="getsensor">&nbsp;</a>

    GET /api/<apikey>/sensors/<id>

Returns the sensor with the specified id.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
{
    "config": {
        "on": true,
        "reachable": true
    },
    "ep": 1,
    "etag": "61eaee2477fc3d5c27932fefeef638bd",
    "manufacturername": "dresden elektronik",
    "mode": 2,
    "modelid": "Lighting Switch",
    "name": "Lighting Switch 1",
    "state": {
        "lastupdated": "2016-07-06T09:39:53"
    },
    "swversion": "1.0",
    "type": "ZHASwitch",
    "uniqueid": "0x00212effff00a6bc"
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
      <td>The config of the sensor.</td>
    </tr>
    <tr>
      <td>config.on</td>
      <td>Bool</td>
      <td>Specifies if the sensor is on or off.</td>
    </tr>
    <tr>
      <td>config.reachable</td>
      <td>Bool</td>
      <td>Specifies if the sensor is reachable.</td>
    </tr>
	<tr>
      <td>config.battery</td>
      <td>Number (0..100)</td>
      <td>The battery status of the sensor.</td>
    </tr>
    <tr>
      <td>ep</td>
      <td>Number</td>
      <td>The Endpoint of the sensor.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../polling#etag">etag</a> which changes whenever the sensor changes.</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>String</td>
      <td>The manufacturer name of the sensor.</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>String</td>
      <td>The model id of the sensor.</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>Number (1|2|3)</td>
      <td>The mode of the sensor (Only available for dresden elektroink Lighting Switch).
        <ul>
          <li>1 = Scenes mode</li>
          <li>2 = Two groups mode</li>
          <li>3 = Color temperature mode</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the sensor..</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Object</td>
      <td>The state of the sensor.</td>
    </tr>
    <tr>
      <td>state.lastupdated</td>
      <td>String</td>
      <td>Timestamp when the sensor was last updated.</td>
    </tr>
    <tr>
      <td>swversion</td>
      <td>String</td>
      <td>Software version of the sensor.</td>
    </tr>
    <tr>
      <td>type</td>
      <td>String</td>
      <td>The type of the sensor.</td>
    </tr>
    <tr>
      <td>uniqueid</td>
      <td>String</td>
      <td>The unique identifiers (MAC address) of the sensor.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Update sensor<a name="update">&nbsp;</a>

    PUT /api/<apikey>/sensors/<id>

Update a sensor with the specified parameters.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the sensor.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>Number (1|2|3)</td>
      <td>Only availabe for dresden elektronik Lighting Switch. Set the mode of the switch.
        <ul>
          <li>1 = Scenes mode</li>
          <li>2 = Two groups mode</li>
          <li>3 = Color temperature mode</li>
        </ul></td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data

    {
      "name": "a nice name"
    }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
    { "success": { "/sensors/1/name": "a nice name" } }
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Change sensor config<a name="changeconfig">&nbsp;</a>

    PUT /api/<apikey>/sensors/<id>/config

Update a sensor config with the specified parameters.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>The on/off status of the sensor.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>reachable</td>
      <td>Bool</td>
      <td>The reachable status of the sensor.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>battery</td>
      <td>Number (1..100)</td>
      <td>The current battery state in percent, only for battery powered devices.</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data

    {
      "on": false,
      "reachable: false
    }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
    { 
      "success": { "/sensors/1/config/on": false } 
      "success": { "/sensors/1/config/reachable": false }
    }
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Change sensor state<a name="changestate">&nbsp;</a>

    PUT /api/<apikey>/sensors/<id>/state

Update a sensor state with the specified parameters.

### Parameters

Allowed sensor types and its states:

<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>Allowed state</th><th>type</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>CLIPSwitch</td>
      <td>buttonevent</td>
      <td>Number</td>
    </tr>
     <tr>
      <td>CLIPOpenClose</td>
      <td>open</td>
      <td>Bool</td>
    </tr>
     <tr>
      <td>CLIPPresence</td>
      <td>presence</td>
      <td>Bool</td>
    </tr>
     <tr>
      <td>CLIPTemperature</td>
      <td>temperature</td>
      <td>Number</td>
    </tr>
     <tr>
      <td>CLIPGenericFlag</td>
      <td>flag</td>
      <td>Bool</td>
    </tr>
     <tr>
      <td>CLIPGenericStatus</td>
      <td>status</td>
      <td>Number</td>
    </tr>
     <tr>
      <td>CLIPHumidity</td>
      <td>humidity</td>
      <td>Number</td>
    </tr>
  </tbody>
</table>

### Example request data

    {
      "flag": false
    }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
    { 
      "success": { "/sensors/1/state/flag": false } 
    }
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Delete sensor<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/sensors/<id>

Delete a sensor.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[{ "success": "1"}]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)
