# KADRILJ roller blind

<p> File: kadrilj_blind.json</p>
<hr/>
## 1. Window covering device

<p> Endpoint: <code> /lights</code></p>
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
      <td>E1752-140</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>KADRILJ roller blind</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>IKEA of Sweden</td>
    </tr>
    <tr>
      <td>type</td>
      <td>Window covering device</td>
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
    <tr>
      <td>lastannounced</td>
      <td>ISO 8601 timestamp</td>
      <td>Timestamp of the last power-cyle or rejoin.</td>
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

### State attributes

<table>
  <thead>
    <tr><th>Attribute</th><th>Datatype</th><th>Description</th><th>Access</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>lift</td>
      <td>UInt8</td>
      <td>The lift state of a roller blind.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>open</td>
      <td>Bool</td>
      <td>The open/close state.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>reachable</td>
      <td>Bool</td>
      <td>When true the device is assumed to be operational.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>bri</td>
      <td>UInt8</td>
      <td>The lift state in earlier versions, use <code class="api-attribute">lift</code> instead. <em class="deprecated">deprecated</em></td>
      <td>RW</td>
    </tr>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>The open state in earlier versions, use <code class="api-attribute">open</code> instead. <em class="deprecated">deprecated</em></td>
      <td>RW</td>
    </tr>
  </tbody>
</table>

### Example output

```
{
  "lastannounced": "2020-12-11T16:57:04Z",
  "lastseen": "2020-12-29T21:55Z",
  "manufacturername": "IKEA of Sweden",
  "modelid": "KADRILJ roller blind",
  "name": "Roller blind 1",
  "state": {
    "bri": 0,
    "lift": 0,
    "on": false,
    "open": true,
    "reachable": true
  },
  "swversion": "20190311",
  "type": "Window covering device",
  "uniqueid": "cc:cc:cc:ff:fe:b3:d9:e6-01"
}
```
<hr/>
## 2. ZHABattery

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
      <td>E1752-140</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>KADRILJ roller blind</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>IKEA of Sweden</td>
    </tr>
    <tr>
      <td>type</td>
      <td>ZHABattery</td>
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
  </tbody>
</table>

### State attributes

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
    "on": true,
    "reachable": true
  },
  "lastseen": "2020-12-29T21:55Z",
  "manufacturername": "IKEA of Sweden",
  "modelid": "KADRILJ roller blind",
  "name": "Roller blind 1",
  "state": {
    "battery": 76,
    "lastupdated": "2020-12-29T21:33:36.229"
  },
  "swversion": "2.2.009",
  "type": "ZHABattery",
  "uniqueid": "cc:cc:cc:ff:fe:b3:d9:e6-01-0001"
}
```
