---
title: Sensors
---

# Sensors

Sensors can be used to measure environment parameters like temperature or to emit events like a button press from a switch. With a coressponding rule they can control lights and groups.

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
      <td>The config of the sensor.
        <ul>
          <li>on - Bool - default: true</li>
          <li>reachable - Bool - default: true</li>
          <li>battery - Number (0&ndash;100)</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

<a name="sensor-types-and-states">&nbsp;</a>
### Supported sensor types and their states

<table class="table table-bordered">
  <thead>
    <tr><th>Sensor type</th><th>Supported state</th><th>Type</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>ZHAAirQuality</td>
      <td>airquality
        <ul>
            <li>Introduced with deCONZ version 2.6.0-beta</li>
        </ul>
      </td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>airqualityppb
        <ul>
            <li>Introduced with deCONZ version 2.6.0-beta</li>
        </ul>
      </td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAAlarm</td>
      <td>alarm</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr>
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
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr>
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
      <td>String</td>
    </tr>
    <tr>
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
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHAHumidity</td>
      <td>humidity</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td>ZHALightLevel</td>
      <td>lux</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
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
    <tr>
      <td></td>
      <td>daylight</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td>ZHAOpenClose</td>
      <td>open</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td>ZHAPower</td>
      <td>current</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>power</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>voltage</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAPresence</td>
      <td>presence</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td>ZHASwitch</td>
      <td>buttonevent</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
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
    <tr>
      <td></td>
      <td>angle</td>
      <td>Number</td>
    </tr>
    <tr>
      <td>ZHAPressure</td>
      <td>pressure</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td>ZHATemperature</td>
      <td>temperature</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td>ZHATime</td>
      <td>lastset</td>
      <td>Time</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>Time</td>
    </tr>
    <tr>
      <td></td>
      <td>localtime</td>
      <td>Time</td>
    </tr>
    <tr>
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
      <td>errorcode
        <ul>
            <li>Introduced with deCONZ version 2.05.81</li>
        </ul>
      </td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>fanmode
        <ul>
            <li>Introduced with deCONZ version 2.6.0-beta</li>
        </ul>
      </td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>floortemperature
        <ul>
            <li>Introduced with deCONZ version 2.05.85</li>
        </ul>
      </td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>heating
        <ul>
            <li>Introduced with deCONZ version 2.05.85</li>
        </ul>
      </td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>lastupdated</td>
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>mountingmodeactive
        <ul>
            <li>Introduced with deCONZ version 2.05.81</li>
        </ul>
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
    <tr>
      <td></td>
      <td>windowopen
        <ul>
            <li>Introduced with deCONZ version 2.05.79</li>
        </ul>
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
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>orientation_x</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>orientation_y</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>orientation_z</td>
      <td>Number</td>
    </tr>
    <tr>
      <td></td>
      <td>tiltangle</td>
      <td>Number</td>
    </tr>
    <tr>
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
      <td>String</td>
    </tr>
    <tr>
      <td></td>
      <td>lowbattery</td>
      <td>Bool</td>
    </tr>
    <tr>
      <td></td>
      <td>tampered</td>
      <td>Bool</td>
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
      <td>The mode of the sensor (only available for dresden elektroink Lighting Switch).
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
      <td>The name of the sensor.</td>
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
      <td>configured</td>
      <td>Bool</td>
      <td>NOT SETTABLE and exclusively for predefined daylight sensor. Determines if the sensor has been configured.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>coolsetpoint</td>
      <td>Number (700&ndash;3500)</td>
      <td>Set the desired cooling temperature for thermostats.
        <ul>
          <li>Introduced with deCONZ version 2.6.0-beta</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>delay</td>
      <td>Number (0&ndash;65535)</td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>displayflipped</td>
      <td>Bool</td>
      <td>Flip the display for TRVs supporting it.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>duration</td>
      <td>Number (0&ndash;65535)</td>
      <td>For ZHAPrensence sensors: time in seconds presence state is set to false again.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>fanmode</td>
      <td>String</td>
      <td>Sets the mode of the fan (exposed for thermostats supporting it).<br><u>Generally supported values are:</u> <b>off, low, medium, high, on, auto, smart</b><br>(Supported modes are device dependent)
        <ul>
          <li>Introduced with deCONZ version 2.6.0-beta</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>groups</td>
      <td>Number</td>
      <td>NOT SETTABLE. Displays the groups associated with the sensor.</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>heatsetpoint</td>
      <td>Number (500&ndash;3200)</td>
      <td>Set the desired heating temperature for thermostats/TRVs.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>hostflags</td>
      <td></td>
      <td></td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>lat</td>
      <td>Number</td>
      <td>NOT SETTABLE and exclusively for predefined daylight sensor. Latitude of the set location/timezone.</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>ledindication</td>
      <td>Bool</td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>localtime</td>
      <td></td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>locked</td>
      <td>Bool</td>
      <td>Child lock active/inactive for thermostats/TRVs supporting it.
        <ul>
          <li>Introduced with deCONZ version 2.05.81</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>long</td>
      <td>Number</td>
      <td>NOT SETTABLE and exclusively for predefined daylight sensor. Longitude of the set location/timezone.</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>String</td>
      <td>Sets the current operating mode of a thermostat.<br><u>Generally supported values are:</u> <b>off, auto, cool, heat, emergency heating, precooling, fan only, dry, sleep</b><br>(Supported modes are device dependent)<br><br>For ubisys S1/S2, operation mode of the switch.<br><u>Supported values are:</u> <b>momentary, rocker</b></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>mountingmode</td>
      <td>Bool</td>
      <td>Sets a TRV into mounting mode if supported (valve fully open position).
        <ul>
          <li>Introduced with deCONZ version 2.05.81</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>The on/off status of the sensor.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>offset</td>
      <td>Number (-32768&ndash;32767)</td>
      <td>Adds a signed offset value to measured temperature and humidity state values. Values send by the REST API are already amended by the offset.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>pending</td>
      <td>Number</td>
      <td>NOT SETTABLE. Bitmap of outstanding configuration tasks for a device. A value of "[]" indicates no outstanding tasks.</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>preset</td>
      <td>String</td>
      <td>Sets the current operating mode for Tuya thermostats.<br><u>Generally supported values are:</u> <b>holiday, auto, manual, comfort, eco, boost, complex</b><br>(Supported modes are device dependent)
        <ul>
          <li>Introduced with deCONZ version 2.05.83</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>reachable</td>
      <td>Bool</td>
      <td>The reachable status of the sensor.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>schedule</td>
      <td></td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>scheduleon</td>
      <td></td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sensitivity</td>
      <td>Number</td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sensitivitymax</td>
      <td>Number</td>
      <td>For Xiaomi vibration sensors, only following 3 values apply: low: 21, medium: 11, high: 1</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sunriseoffset</td>
      <td>Number (-120&ndash;120)</td>
      <td>NOT SETTABLE and exclusively for predefined daylight sensor. Sunrise offset value for location/timezone in minutes.</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>sunsetoffset</td>
      <td>Number (-120&ndash;120)</td>
      <td>NOT SETTABLE and exclusively for predefined daylight sensor. Sunset offset value for location/timezone in minutes.</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>swingmode</td>
      <td>String</td>
      <td>Sets the AC louvers position (exposed for thermostats supporting it).<br><u>Generally supported values are:</u> <b>fully closed, fully open, quarter open, half open, three quarters open</b>
        <ul>
          <li>Introduced with deCONZ version 2.6.0-beta</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>temperature</td>
      <td>Number (-27315&ndash;32767)</td>
      <td>NOT SETTABLE. Reported temperature values by Xiaomi devices which are no temperature measuring devices (presumably device temperature).</td>
      <td>Display only</td>
    </tr>
    <tr>
      <td>temperaturemeasurement</td>
      <td>String</td>
      <td>Sets the mode of operation for Elko Super TR thermostat.<br><u>Generally supported values are:</u> <b>air sensor, floor sensor, floor protection</b>
        <ul>
          <li>Introduced with deCONZ version 2.05.85</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>tholddark</td>
      <td>Number (0&ndash;65534)</td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>tholdoffset</td>
      <td>Number (1&ndash;65534)</td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>usertest</td>
      <td>Bool</td>
      <td></td>
      <td>optional</td>
    </tr>
    <tr>
      <td>windowcoveringtype</td>
      <td>Number (0&ndash;9)</td>
      <td>Sets the covering type and starts calibration for ubisys J1.<br><u>Supported values are:</u><br><b>0</b> (Roller Shade),<br><b>1</b> (Roller Shade two motors),<br><b>2</b> (Roller Shade exterior),<br><b>3</b> (Roller Shade two motors ext),<br><b>4</b> (Drapery),<br><b>5</b> (Awning),<br><b>6</b> (Shutter),<br><b>7</b> (Tilt Blind Lift only),<br><b>8</b> (Tilt Blind lift & tilt),<br><b>9</b> (Projector Screen)</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>windowopen_set</td>
      <td>Bool</td>
      <td>Sets if window open detection shall be active/inactive for Tuya thermostats.<br>(Support is device dependent)
        <ul>
          <li>Introduced with deCONZ version 2.05.83</li>
        </ul>
      </td>
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
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": "1" } ]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)