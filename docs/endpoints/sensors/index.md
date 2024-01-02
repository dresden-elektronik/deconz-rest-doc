---
title: Sensors
---

# Sensors

Sensors can be used to measure environment parameters like temperature or to emit events like a button press from a switch. With a coressponding rule they can control lights and groups.

## Create sensor<a name="create">&nbsp;</a>

    POST /api/<apikey>/sensors

Creates a new CLIP sensor.

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
      <td>The type of the sensor, see <a href="#sensor-types-and-states">Sensor types and states</a>.</td>
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
      <td>The state of the sensor, see <a href="#sensor-types-and-states">Sensor types and states</a>.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>config</td>
      <td>Object</td>
      <td>
        <p>The config of the sensor.</p>
        <ul class="value-list">
          <li><code class="api-attribute">on</code> &mdash; Bool (default: true)</li>
          <li><code  class="api-attribute">reachable</code> &mdash; Bool (default: true)</li>
          <li><code  class="api-attribute">battery</code> &mdash; Number (0&ndash;100)</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data

<pre class="highlight">
<code>
{
    "config": {
        "on": true,
        "reachable": true
    },
    "manufacturername": "Me",
    "modelid": "T1000",
    "name": "My Switch",
    "swversion": "1.0",
    "type": "CLIPSwitch",
    "uniqueid": "00:1f:ee:00:00:00:08:bb-01-1000"
}
</code>
</pre>

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "1" } } ]
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

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get all Sensors<a name="getall">&nbsp;</a>

    GET /api/<apikey>/sensors

Returns a list of all sensors. If there are no sensors in the system an empty object {} is returned.

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
    "1": {
        "config": {
            "on": true,
            "reachable": true
        },
        "ep": 1,
        "etag": "61eaee2477fc3d5c27932fefeef638bd",
        "lastseen": "2016-07-06T09:39Z",
        "manufacturername": "dresden elektronik",
        "modelid": "Lighting Switch",
        "name": "Lighting Switch 1",
        "state": {
            "lastupdated": "2016-07-06T09:39:53"
        },
        "swversion": "1.0",
        "type": "ZHASwitch",
        "uniqueid": "00:21:2e:ff:ff:00:a6:bc-01-1000"
    },

    "2": {
        "config": {
            "on": true,
            "reachable": true
        },
        "ep": 2,
        "etag": "61eaee2477fc3d5c27932fefeef638bd",
        "lastseen": "2016-07-06T09:39Z",
        "manufacturername": "dresden elektronik",
        "modelid": "Lighting Switch",
        "name": "Lighting Switch 2",
        "state": {
            "lastupdated": "2016-07-06T09:39:53"
        },
        "swversion": "1.0",
        "type": "ZHASwitch",
        "uniqueid": "00:21:2e:ff:ff:00:a6:bc-02-1000"
    }
}
</code>
</pre>

#### Response fields

The whole sensor object as descripted in [Get sensor](#getsensor).

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get sensor<a name="getsensor">&nbsp;</a>

    GET /api/<apikey>/sensors/<id>

Returns the sensor with the specified id.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
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
    "lastseen": "2016-07-06T09:39Z",
    "manufacturername": "dresden elektronik",
    "mode": 2,
    "modelid": "Lighting Switch",
    "name": "Lighting Switch 1",
    "state": {
        "lastupdated": "2016-07-06T09:39:53"
    },
    "swversion": "1.0",
    "type": "ZHASwitch",
    "uniqueid": "00:21:2e:ff:ff:00:a6:bc-01-1000"
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
      <td>The config of the sensor. Refer to <a href="#changeconfig">Change sensor config</a> for further details.</td>
    </tr>
    <tr>
      <td>ep</td>
      <td>Number</td>
      <td>The Endpoint of the sensor.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../../misc/polling#etag">etag</a> which changes whenever the sensor changes.</td>
    </tr>
    <tr>
      <td>lastseen</td>
      <td>ISO 8601 timestamp</td>
      <td>Timestamp representing the last time a message from the sensor was received. UTC with resolution of minutes.</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>String</td>
      <td>The manufacturer name of the sensor.</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>Number</td>
      <td>
        <p>The mode of the sensor.</p>
        <ul class="value-list">
          <li>1 = Scenes mode</li>
          <li>2 = Two groups mode</li>
          <li>3 = Color temperature mode</li>
        </ul>
        (only available for dresden elektronik Lighting Switch)
      </td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>String</td>
      <td>The model id of the sensor.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the sensor.</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Object</td>
      <td>The state of the sensor.</td>
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
      <td>The unique identifiers including the MAC address of the sensor.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

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
      <td>Number</td>
      <td>
        <p>Only availabe for dresden elektronik Lighting Switch. Set the mode of the switch.</p>
        <ul class="value-list">
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
<code class="no-highlight">
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

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Change sensor config<a name="changeconfig">&nbsp;</a>

    PUT /api/<apikey>/sensors/<id>/config

Update a sensor config with the specified parameters.<br>
Sensors expose certain configuration parameters depending on their defined or known capabilities. To get an overview on which parameters are available for a particular device, get the sensor state of either all [Get all sensors](#getall) or a single sensor [Get sensor](#getsensor).

### Parameters

**Important:** Most attributes can be found in [Supported config attributes](#dev-sensor-config-attr)

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>battery</td>
      <td>Number (1&ndash;100)</td>
      <td>The current battery state in percent, only for battery powered devices.</td>
      <td>optional</td>
    </tr>
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
  </tbody>
</table>

### Example request data

    {
      "on": false,
      "reachable": false
    }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
    {
      "success": { "/sensors/1/config/on": false },
      "success": { "/sensors/1/config/reachable": false }
    }
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Change sensor state<a name="changestate">&nbsp;</a>

    PUT /api/<apikey>/sensors/<id>/state

Update a sensor state with the specified parameters.

!!! note
    Changing the sensor state is only allowed for CLIP sensors.

### Parameters

Allowed parameters are listed in <a href="#clip-sensor-types-and-states">CLIP sensors</a>.

### Example request data

    {
      "flag": false
    }

### Response
<pre class="headers">
<code class="no-highlight">
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

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Delete sensor<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/sensors/<id>

Delete a sensor.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>reset</td>
      <td>Bool</td>
      <td>If this parameter is omitted, it will implicitly be set to false and the sensor is marked as deleted in the database. If set to true, deCONZ is trying to reset the whole physical device by issuing a leave request. It is required that the device is awake (able to receive commands) or supports this type of request respectively and on success, the device is deleted as a node and reset to factory defaults.</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Response

Response when no reset option provided.

<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "1" } } ]
</code>
</pre>

Response when reset option is provided.
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "/sensors/1/reset": false } } ]
</code>
</pre>


### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

<a name="sensor-types-and-states">&nbsp;</a>
## Supported sensor types and states

<a name="clip-sensor-types-and-states">&nbsp;</a>
### CLIP sensors

These are virtual sensors without a real device behind it. CLIP sensors can be created, modified and used in rules.

#### Supported state attributes

<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>State attribute</th><th>Type</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>CLIPAlarm</td>
      <td>alarm</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>CLIPBattery</td>
      <td>battery</td>
      <td>Number (uint8)</td>
    </tr>
    <tr>
      <td>CLIPCarbonMonoxide</td>
      <td>carbonmonoxide</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>CLIPConsumption</td>
      <td>consumption</td>
      <td>Number (uint64)</td>
    </tr>
    <tr>
      <td>CLIPFire</td>
      <td>fire</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>CLIPGenericFlag</td>
      <td>flag</td>
      <td>Bool</td>
    </tr>
     <tr>
      <td>CLIPGenericStatus</td>
      <td>status</td>
      <td>Int32</td>
    </tr>
    <tr>
      <td>CLIPHumidity</td>
      <td>humidity</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td>CLIPLightLevel</td>
      <td>lightlevel</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td></td>
      <td>lux</td>
      <td>Uint32</td>
    </tr>
    <tr>
      <td></td>
      <td>dark</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>daylight</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>CLIPOpenClose</td>
      <td>open</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>CLIPPower</td>
      <td>power</td>
      <td>Int16</td>
    </tr>
    <tr>
      <td></td>
      <td>voltage</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td></td>
      <td>current</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td>CLIPPresence</td>
      <td>presence</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>duration</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td>CLIPPressure</td>
      <td>pressure</td>
      <td>Int16</td>
    </tr>
    <tr>
      <td>CLIPSwitch</td>
      <td>buttonevent</td>
      <td>Uint32</td>
    </tr>
    <tr>
      <td>CLIPTemperature</td>
      <td>temperature</td>
      <td>Int16</td>
    </tr>
    <tr>
      <td>CLIPVibration</td>
      <td>vibration</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>CLIPWater</td>
      <td>water</td>
      <td>Bool</td>
    </tr>
  </tbody>
</table>

#### Supported config attributes
<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>Config attribute</th><th>Type</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>CLIPHumidity</td>
      <td>offset</td>
      <td>Int16</td>
    </tr>
    <tr>
      <td>CLIPLightLevel</td>
      <td>tholddark</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td></td>
      <td>tholddarkoffset</td>
      <td>Uint16</td>
    </tr>
    <tr>
      <td>CLIPTemperature</td>
      <td>offset</td>
      <td>Int16</td>
    </tr>
  </tbody>
</table>

### Device sensors

#### Supported state attributes

<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>State attribute</th><th>Type</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>ZHAAirQuality</td>
      <td data-since="v2.6.0-beta">airquality</td>
      <td>String
        <hr/>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"excellent"</li>
          <li>"good"</li>
          <li>"moderate"</li>
          <li>"poor"</li>
          <li>"unhealthy"</li>
          <li>"out of scale"</li>
        </ul>
      </td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td data-since="v2.6.0-beta">airqualityppb
      </td>
      <td>Uint16 (0&ndash;65534)</td>
    </tr>
    <tr>
      <td>ZHAAlarm</td>
      <td>alarm</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHACarbonMonoxide</td>
      <td>carbonmonoxide</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHAConsumption</td>
      <td>consumption</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>power</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAFire</td>
      <td>fire</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHAHumidity</td>
      <td>humidity</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td>ZHALightLevel</td>
      <td>lux</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lightlevel</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>dark</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>daylight</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHAOpenClose</td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>open</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHAPower</td>
      <td>current</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>power</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>voltage</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAPresence</td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>presence</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHASwitch</td>
      <td>
        <p>buttonevent<p>
        <hr/>
        <p>Refer to <a href="./button_events">Button Events</a> for<br/> device specific values.</p>
      </td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>gesture</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>eventduration</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>x</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>y</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>angle</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAPressure</td>
      <td>pressure</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td>ZHATemperature</td>
      <td>temperature</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td>ZHATime</td>
      <td>lastset</td>
      <td>Time</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>localtime</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>utc</td>
      <td>Time</td>
    </tr>
    <tr>
      <td>ZHAThermostat</td>
      <td>on</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td data-since="v2.5.81">errorcode
      </td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td data-since="v2.6.0-beta">fanmode
      </td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td data-since="v2.5.85">floortemperature
      </td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td data-since="v2.5.85">heating
      </td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td data-since="v2.5.81">mountingmodeactive
      </td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>temperature</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>valve</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td data-since="v2.5.79">windowopen
      </td>
      <td>String</td>
    </tr>
    <tr>
      <td>ZHAVibration</td>
      <td>vibration</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>orientation</td>
      <td>Array of 3 Numbers</td>
    </tr>
    <tr>
      <td></td>
      <td>tiltangle</td>
      <td>Number</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>vibrationstrength</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAWater</td>
      <td>water</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>Various sensors</td>
      <td data-since="v2.15.0-beta">charging</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>Various sensors</td>
      <td data-since="v2.16.1">presenceevent</td>
      <td>String</td>
    </tr>
  </tbody>
</table>

<a name="dev-sensor-config-attr">&nbsp;</a>
#### Supported config attributes
<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>Config attribute</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Daylight</td>
      <td>configured</td>
      <td>Bool</td>
      <td>True if the daylight sensor is configured with coordinates.</td>
      <td>R</td>
    </tr>
    <tr>
      <td></td>
      <td>lat</td>
      <td>Number</td>
      <td>Latitude of the set location/timezone.</td>
      <td>W</td>
    </tr>
    <tr>
      <td></td>
      <td>long</td>
      <td>Number</td>
      <td>Longitude of the set location/timezone.</td>
      <td>W</td>
    </tr>
    <tr>
      <td></td>
      <td>sunriseoffset</td>
      <td>Number (-120&ndash;120)</td>
      <td>Sunrise offset value for location/timezone in minutes.</td>
      <td>R</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>sunsetoffset</td>
      <td>Number (-120&ndash;120)</td>
      <td>Sunset offset value for location/timezone in minutes.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>ZHALightLevel</td>
      <td>tholddark</td>
      <td>Number (0&ndash;65534)</td>
      <td>
        <p>Specifies at which <code class="api-attribute">lightlevel</code> the <code class="api-attribute">dark</code> attribute turns false.</p>
        <p>Default: 12000</p>
      </td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>tholdoffset</td>
      <td>Number (1&ndash;65534)</td>
      <td>
        <p>Relative offset to <code class="api-attribute">tholddark</code>. Sets <code class="api-attribute">daylight</code> attribute to true when when lightlevel is at or above (tholddark + tholdoffset).</p>
        <p>Default: 7000</p>
      </td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td>ZHAHumidity</td>
      <td>offset</td>
      <td>Number (-32768&ndash;32767)</td>
      <td>Adds a signed offset value to measured state values. Values send by the REST-API are already amended by the offset.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>ZHAPresence</td>
      <td>duration</td>
      <td>Number (0&ndash;65535)</td>
      <td>Timeout in seconds presence state is set to false again.</td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>delay</td>
      <td>Uint16 (0&ndash;65535)</td>
      <td>
        <p>The occupied to unoccupied delay in seconds.</p>
      </td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td>ZHATemperature</td>
      <td>offset</td>
      <td>Number (-32768&ndash;32767)</td>
      <td>Adds a signed offset value to measured state values. Values send by the REST-API are already amended by the offset.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>ZHASwitch</td>
      <td>group</td>
      <td>Uint16</td>
      <td>
        <p>The associated Zigbee group the sensor controls.</p>
        <p>(only supported by some sensors)</p>
      </td>
      <td>R</td>
    </tr>
    <tr>
      <td></td>
      <td>mode</td>
      <td>String</td>
      <td>
        <p>For ubisys S1/S2, operation mode of the switch.</p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"momentary"</li>
          <li>"rocker"</li>
        </ul>
      </td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td>
        <p>Ubisys J1</p>(ZHASwitch)</td>
      <td>window coveringtype</td>
      <td>Number (0&ndash;9)</td>
      <td>
        <p>Sets the covering type and starts calibration.</p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>0 = Roller Shade</li>
          <li>1 = Roller Shade two motors</li>
          <li>2 = Roller Shade exterior</li>
          <li>3 = Roller Shade two motors ext</li>
          <li>4 = Drapery</li>
          <li>5 = Awning</li>
          <li>6 = Shutter</li>
          <li>7 = Tilt Blind Lift only</li>
          <li>8 = Tilt Blind lift & tilt</li>
          <li>9 = Projector Screen
        </ul>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td>ZHAThermostat</td>
      <td>mode</td>
      <td>String</td>
      <td>
        <p>Sets the current operating mode of a thermostat.<p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"off"</li>
          <li>"auto"</li>
          <li>"cool"</li>
          <li>"heat"</li>
          <li>"emergency heating"</li>
          <li>"precooling"</li>
          <li>"fan only"</li>
          <li>"dry"</li>
          <li>"sleep"</li>
        </ul>
        <p>(Supported modes are device dependent)</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>displayflipped</td>
      <td>Bool</td>
      <td>Flip the display for TRVs supporting it.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>externalsensortemp</td>
      <td>Number (-32768&ndash;32767)</td>
      <td data-since="v2.10.0-beta">
        <p>Allows to use the temperature value provided by an external sensor.</p>

        (device dependent and only exposed for devices supporting it)
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>externalwindowopen</td>
      <td>Bool</td>
      <td data-since="v2.10.2-beta">
        <p>Allows to use the open/close state from an external sensor.</p>

        (device dependent and only exposed for devices supporting it)
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>fanmode</td>
      <td>String</td>
      <td data-since="v2.6.0-beta">
        <p>Sets the mode of the fan.</p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"off"</li>
          <li>"low"</li>
          <li>"medium"</li>
          <li>"high"</li>
          <li>"on"</li>
          <li>"auto"</li>
          <li>"smart"</li>
        </ul>

        (device dependent and only exposed for devices supporting it)
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>hostflags</td>
      <td>Uint32</td>
      <td>
        <p>Eurotronic Spirit SPZB</p>
        <ul class="value-list">
          <li>0x0002 &mdash; Display flipped</li>
          <li>0x0004 &mdash; Mode heat</li>
          <li>0x0010 &mdash; Mode off</li>
          <li>0x0080 &mdash; Locked</li>
        </ul>
        <p>Only for debugging purpose.</p>
      </td>
      <td>R</td>
    </tr>
    <tr>
      <td></td>
      <td>locked</td>
      <td>Bool</td>
      <td data-since="v2.5.81">Child lock active/inactive for thermostats/TRVs supporting it.
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>preset</td>
      <td>String</td>
      <td data-since="v2.5.83">
        <p>Sets the operating mode for Tuya thermostats.</p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"holiday"</li>
          <li>"auto"
          <li>"manual"</li>
          <li>"comfort"</li>
          <li>"eco"</li>
          <li>"boost"</li>
          <li>"complex"</li>
        </ul>
        <p>(supported modes are device dependent)</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>setvalve</td>
      <td>Bool</td>
      <td data-since="v2.6.0-beta">
        <p>Controls valve of thermostats.</p>
        <ul class="value-list">
          <li>false &mdash; Close valve</li>
          <li>true &mdash; Open valve</li>
        </ul>
        (exposed for thermostats supporting it)
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>swingmode</td>
      <td>String</td>
      <td data-since="v2.6.0-beta">
        <p>Sets the AC louvers position.</p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"fully closed"</li>
          <li>"fully open"</li>
          <li>"quarter open"</li>
          <li>"half open"</li>
          <li>"three quarters open"</li>
        </ul>
        (exposed for thermostats supporting it)
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>temperature measurement</td>
      <td>String</td>
      <td data-since="v2.5.85">
        <p>Sets the mode of operation for Elko Super TR thermostat.</p>
        <p>Supported values:</p>
        <ul class="value-list">
          <li>"air sensor"</li>
          <li>"floor sensor"</li>
          <li>"floor protection"</li>
        </ul>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>window open_set</td>
      <td>Bool</td>
      <td data-since="v2.5.83">
        <p>Sets if window open detection shall be active or inactive for Tuya thermostats.</p>
        <p>(support is device dependent)</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>schedule</td>
      <td>Array</td>
      <td>
        <p>A thermostat schedule.</p>
        <mark>todo: describe</mark>
     </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>schedule_on</td>
      <td>Bool</td>
      <td>True when a thermostat schedule is enabled.</td>
      <td>RW</td>
    </tr>
   <tr>
      <td></td>
      <td>coolsetpoint</td>
      <td>Number (700&ndash;3500)</td>
      <td data-since="v2.6.0-beta">Set the desired cooling temperature.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>heatsetpoint</td>
      <td>Number (500&ndash;3200)</td>
      <td>Set the desired heating temperature.</td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>mountingmode</td>
      <td>Bool</td>
      <td data-since="v2.5.81">Sets a TRV into mounting mode if supported (valve fully open position).</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>Various sensors</td>
      <td>clickmode</td>
      <td>String</td>
      <td data-since="v2.15.0-beta">
        <p>Intended for devices which can configure the click behavior of a button.</p>
        <p>Xiaomi devices have possible values of 'coupled', 'decoupled', 'multiclick' and 'highspeed'.</p>
        <p>(only supported by some sensors)</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>devicemode</td>
      <td>String</td>
      <td data-since="v2.15.0-beta">
        <p>Intended for devices which can change their mode of operation.</p>
        <p>Xiaomi devices have possible values of 'compatibility' and 'zigbee'.</p>
        <p>(only supported by some sensors, shouldn't be changed)</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>enrolled</td>
      <td>Number</td>
      <td data-since="v2.9.1-beta">
        <p>Displays the current IAS enrollment status.</p>
        <p>Supported for all devices having the IAS Zone cluster:</p>
        <ul class="value-list">
           <li>0 = Init</li>
           <li>1 = Enrolled</li>
           <li>2 = Read</li>
           <li>3 = Wait read</li>
           <li>4 = Write CIE address</li>
           <li>5 = Wait write CIE address</li>
           <li>6 = Delay enroll</li>
           <li>7 = Enroll</li>
           <li>8 = Wait enroll</li>
           <li>9 = Max (invalid)</li>
        </ul>
      </td>
      <td>R</td>
    </tr>
    <tr>
      <td></td>
      <td>ledindication</td>
      <td>Bool</td>
      <td>
        <p>Lets the sensor indicate itself, usually via LED blinking.</p>
        <p>Supported for Philips Hue motion sensor.</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>pending</td>
      <td>Uint8</td>
      <td>Bitmap of outstanding configuration tasks for a device. A value of "[]" indicates no outstanding tasks.
        <mark>todo: describe possibe values</mark>
      </td>
      <td>R</td>
    </tr>
    <tr>
      <td></td>
      <td>resetpresence</td>
      <td>Bool</td>
      <td data-since="v2.16.1">
        <p>Resets the presence state of the Xiaomi FP1 presence sensor.</p>
      </td>
      <td>W</td>
    </tr>
    <tr>
      <td></td>
      <td>sensitivity</td>
      <td>Number</td>
      <td>
        <p>Device specific sensitivity, with following supported values.</p>
        <p>Philips Hue motion sensor:</p>
        <ul class="value-list">
           <li>0 = low</li>
           <li>1 = medium</li>
           <li>2 = high</li>
        </ul>

        <p>Xiaomi vibration sensor:</p>
        <ul class="value-list">
           <li>21 = low</li>
           <li>11 = medium</li>
           <li>&nbsp;&nbsp;1 = high</li>
        </ul>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>sensitivitymax</td>
      <td>Number</td>
      <td>
        Device specific maximum <code class="api-attribute">sensitivity</code> value.
        <p>Xiaomi vibration sensor:&nbsp;21</p>
        <p>Philips Hue motion sensor:&nbsp;2</p>
      </td>
      <td>R</td>
    </tr>
    <tr>
      <td></td>
      <td>triggerdistance</td>
      <td>String</td>
      <td data-since="v2.16.1">
        <p>A device specific distance setting when it triggers the associated function (e.g. detect presence or motion).</p>
      </td>
      <td>RW</td>
    </tr>
    <tr class="strong-border-bottom">
      <td></td>
      <td>usertest</td>
      <td>Bool</td>
      <td>
        <p>Starts the sensor self-test mode.</p>
        <p>Supported for Philips Hue motion sensor.</p>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td>Xiaomi sensors</td>
      <td>temperature</td>
      <td>Number (-27315&ndash;32767)</td>
      <td>
        <p>Reported temperature values by devices which are no temperature measuring devices.</p>
        <p>(presumably device temperature).</p>
      </td>
      <td>R</td>
    </tr>
    <tr>
      <td>Develco Metering Interfaces</td>
      <td>interfacemode</td>
      <td>Number</td>
      <td data-since="v2.10.3-beta">
        <p>Allows to set the device specific interface mode.</p>
        <p>ZHEMI101:</p>
        <ul class="value-list">
           <li>1 = Pulse Counting on an Electricity Meter – Unit KWh</li>
           <li>2 = Pulse Counting on a Gas Meter – Unit m3</li>
           <li>3 = Pulse Counting on a Water Meter – Unit m3</li>
           <li>4 = Kamstrup KMP Protocol</li>
           <li>5 = Not Supported - Linky Protocol</li>
           <li>6 = DLMS-COSEM - IEC62056-21 mod A</li>
           <li>7 = P1 Dutch Standard – DSMR 2.3 Version</li>
           <li>8 = P1 Dutch Standard – DSMR 4.0 Version</li>
        </ul>
        <p>EMIZB-132:</p>
        <ul class="value-list">
           <li>1 = Norwegian HAN</li>
           <li>2 = Norwegian HAN – Enable extra load</li>
           <li>3 = Aidon Meter supporting Norwegian HAN HW interface</li>
           <li>4 = Kaifa meter and Kamstrup meters running old firmware</li>
           <li>5 = Auto detect meter function</li>
        </ul>

        (device dependent and only exposed for devices supporting it)
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td></td>
      <td>pulseconfiguration</td>
      <td>Number (0&ndash;65535)</td>
      <td data-since="v2.10.3-beta">
        <p>Pulse Configuration represents the number of pulses the meter outputs per unit.</p>

        (device dependent and only exposed for devices supporting it)
      </td>
      <td>RW</td>
    </tr>
  </tbody>
</table>