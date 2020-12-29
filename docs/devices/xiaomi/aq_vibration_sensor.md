# Vibration sensor DJT11LM

<p> File: aq1_vibration_sensor.json</p>
<hr/>
## 1. ZHAVibration

<p> Endpoint: <code> /sensors</code></p>
### Device information

<table>
  <thead>
    <tr><th>Attribute</th><th>Value</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>status</td>
      <td>Bronze</td>
    </tr>
    <tr>
      <td>product</td>
      <td>DJT11LM</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>lumi.vibration.aq1</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>LUMI</td>
    </tr>
    <tr>
      <td>type</td>
      <td>ZHAVibration</td>
    </tr>
  </tbody>
</table>

### Top level attributes

<table>
  <thead>
    <tr><th>Attribute</th><th>Datatype</th><th>Description</th><th>Access</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>lastseen</td>
      <td>ISO 8601 timestamp</td>
      <td>Timestamp of the last communication.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>String</td>
      <td>Manufacturer name of the device.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>String</td>
      <td>Model identifier of the device.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of the resource.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>swversion</td>
      <td>String</td>
      <td>Firmware version of the device.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>type</td>
      <td>String</td>
      <td>Type of the resource.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>uniqueid</td>
      <td>String</td>
      <td>Unique identifier of the resource.</td>
      <td>R</td>
    </tr>
  </tbody>
</table>

### Config attributes

<table>
  <thead>
    <tr><th>Attribute</th><th>Datatype</th><th>Description</th><th>Access</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>When true the sensor is enabled in rules.<p>  Default: true</p>
</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>reachable</td>
      <td>Bool</td>
      <td>When true the device is assumed to be operational.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>pending</td>
      <td>Array</td>
      <td>Pending tasks to configure the device.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>battery</td>
      <td>UInt8</td>
      <td>The current device battery level.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>temperature</td>
      <td>UInt8</td>
      <td>The current device temperature in °C.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>sensitivity</td>
      <td>UInt8</td>
      <td>The sensor sensitivity.<ul class="value-list">
<li>low &mdash; 21</li>
<li>medium &mdash; 11</li>
<li>high &mdash; 1</li>
</ul>
</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>sensitivitymax</td>
      <td>UInt8</td>
      <td>The maximum sensor sensitivity.<p>  Default: 21</p>
</td>
      <td>RW</td>
    </tr>
  </tbody>
</table>

### State attributes

<table>
  <thead>
    <tr><th>Attribute</th><th>Datatype</th><th>Description</th><th>Access</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>orientation</td>
      <td>Array[3]</td>
      <td>The orientation in degrees [X, Y, Z]. <br/> Where X, Y, Z can be in range -90&ndash;90.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>tiltangle</td>
      <td>UInt16</td>
      <td>The current tilt angle.<p>  Default: 0</p>
</td>
      <td>R</td>
    </tr>
    <tr>
      <td>vibration</td>
      <td>Bool</td>
      <td>True when vibration is detected.<p>  Default: false</p>
</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>vibrationstrength</td>
      <td>UInt16</td>
      <td>The strength of the detected vibration.<p>  Default: 0</p>
</td>
      <td>R</td>
    </tr>
    <tr>
      <td>lastupdated</td>
      <td>ISO 8601 timestamp</td>
      <td>Timestamp when state was last updated.</td>
      <td>R</td>
    </tr>
  </tbody>
</table>

### Example output

```
{
  "config": {
    "battery": 95,
    "on": true,
    "pending": [],
    "reachable": true,
    "sensitivity": 1,
    "sensitivitymax": 21,
    "temperature": 2800
  },
  "lastseen": "2020-12-29T22:03Z",
  "manufacturername": "LUMI",
  "modelid": "lumi.vibration.aq1",
  "name": "Vibration Sensor",
  "state": {
    "lastupdated": "2020-12-29T22:02:50.534",
    "orientation": [
      81,
      1,
      9
    ],
    "tiltangle": 84,
    "vibration": false,
    "vibrationstrength": 11
  },
  "swversion": "20180130",
  "type": "ZHAVibration",
  "uniqueid": "00:15:8d:00:02:af:95:f9-01-0101"
}
```
<hr/>
## Known Issues


### Sticky Parents

Almost all Xiaomi end-devices stick to their parent after pairing.
The parent is the device which repeats the signal, it can be a router or the coordinator.

Once a parent is cut from power or otherwise lost, the end-device won't automatically search for a new parent and appears to be offline.

&rarr; Best practice for pairing is therefore to pair the device at the place where it's gonna be installed to force it to select a *good* parent. It's also advisable to power off all routers which aren't powered all the time, so that they aren't considered as parent when pairing.
