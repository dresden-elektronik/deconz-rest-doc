# Motion sensor ESS-SI-PIR-6101

<p> File: rh3040_motion_sensor.json</p>
<hr/>
## 1. ZHAPresence

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
      <td>ESS-SI-PIR-6101</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>RH3040</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>Tuyatec</td>
    </tr>
    <tr>
      <td>type</td>
      <td>ZHAPresence</td>
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
      <td>Todo not shown in output?</td>
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
    <tr>
      <td>lastseen</td>
      <td>ISO 8601 timestamp</td>
      <td>Timestamp of the last communication.</td>
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
      <td>battery</td>
      <td>UInt8</td>
      <td>The current device battery level.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>duration</td>
      <td>UInt16</td>
      <td>The duration until presence is automatically turned back to false.<p>  Default: 120</p>
</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>When true the sensor is enabled in rules.<p>  Default: true</p>
</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>pending</td>
      <td>Array</td>
      <td>Pending tasks to configure the device.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>reachable</td>
      <td>Bool</td>
      <td>When true the device is assumed to be operational.</td>
      <td>R</td>
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
      <td>presence</td>
      <td>Bool</td>
      <td>The current presence state.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>lowbattery</td>
      <td>Bool</td>
      <td>True when the device battery runs low.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>tampered</td>
      <td>Bool</td>
      <td>True when the device tampered alarm was triggered.</td>
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
    "battery": 75,
    "duration": 120,
    "on": true,
    "pending": [],
    "reachable": true
  },
  "lastseen": "2020-12-29T14:47Z",
  "manufacturername": "Tuyatec",
  "modelid": "RH3040",
  "name": "Presence 68",
  "state": {
    "lastupdated": "2020-12-29T14:47:19.022",
    "lowbattery": false,
    "presence": true,
    "tampered": false
  },
  "type": "ZHAPresence",
  "uniqueid": "14:b4:57:ff:fe:15:66:fc-01-0500"
}
```
