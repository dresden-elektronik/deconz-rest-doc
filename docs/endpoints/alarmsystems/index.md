---
title: Alarm Systems
---

# Alarm Systems

<mark>Work in progress</mark>

!!! Important
    This page serves as a Request For Comments (RFC); the API is not available in any release yet.

An alarm system uses sensors and keypads to implement a stateful security system. It can be disarmed, armed, and raises events when an alarm is triggered.


Arming and disarming is done by:

* REST-API request
* Keypads via PIN code
* Keyfobs


Alarms are be triggered by:

* Motion sensors
* Open/close sensors
* Vibration sensors
* Switch button events
* Light state changes
* Externally via REST-API

An alarm system simplifies the configuration of a Zigbee security system for REST-API clients. It aligns with the design of traditional security systems, allowing to bridge with integrations in home automation systems like:

* Homebridge <https://www.npmjs.com/package/homebridge-alarm-panel>
* Home Assistant <https://www.home-assistant.io/integrations/manual>

## Basics

The alarm systems REST-API is designed with the following high level principles.

### Arm modes

There are four arm modes which determine when alarms are triggered.


<table class="table table-bordered">
  <thead>
    <tr><th>Arm mode</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>disarmed</code></td>
      <td>No alarms are triggered, and the system is inactive.</td>
    </tr>
    <tr>
      <td><code>armed_away</code></td>
      <td>Alarms are triggered by all devices in the inner and outer perimeter.</td>
    </tr>
    <tr>
      <td><code>armed_stay</code></td>
      <td>Alarms are triggered only by the outer perimeter, e.g. the door open/close sensor or a vibration sensor to detect glass break of a window. Devices in the inner perimeter, like an presence sensor in the kitchen won't trigger an alarm.</td>
    </tr>
    <tr>
      <td><code>armed_night</code></td>
      <td>Similar to <code>armed_stay</code>, this mode includes additional devices, which are usually not approached at night, e.g. the window open/close sensor of the living room.</td>
    </tr>
  </tbody>
</table>

### Entry and exit delays

Each arm mode has configurable entry and exit delays, in the range of 0–255 seconds.

* **Exit delays** allow leaving the house, after arming the alarm system, without triggering an alarm.<br/>
* **Entry delays** allow entering the house while the alarm system is armed, to disarm it before an alarm is triggered.


### Alarm trigger durations

Each arm mode has a configurable trigger duration, in the range of 0–255 seconds.

A trigger duration determines how long a alarm system stays in the `in_alarm` state, when an alarm is triggered. For example, when an alarm is triggered in the `armed_away` state, the alarm system moves to the `in_alarm` state for 120 seconds (default alarm trigger duration), and generates events, after that it returns to the `armed_away` state.


### PIN codes

A PIN code protects arming and disarming the alarm system. It's compared to the entered code of keypads and REST-API requests for arming and disarming.

**Important:** PIN codes are configured for whole alarm system, not a single keypad. Multiple keypads, as well as the REST-API refer to the same PIN codes.

Currently only one PIN code, aka "code0", is supported. In future multiple PIN codes can be configured. Internally a PIN code has the state "enabled" or "disabled". This makes it possible to dynamically enable a PIN code, for example a rule enables the guest PIN code on weekends.



## Create alarm system<a name="create">&nbsp;</a>

    POST /api/<apikey>/alarmsystems

Creates a new alarm system. After creation the arm mode is set to `disarmed`.

!!! Note
    This is only needed than more than one alarm system is needed. The "default" alarm system with id "1" is created automatically.

    Running multiple alarm systems is useful to seperate areas, for example: One alarm system for the house, and one for the guest house. Each with their own keypads and PIN codes.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the new alarm system</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data
    { "name": "Guest house alarm system" }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "2" } } ]
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
      <td>The unique identifier of the alarm system.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get all alarm systems<a name="getall">&nbsp;</a>

    GET /api/<apikey>/alarmsystems

Returns a list of all alarm systems.

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
    "name": "default",
    "config": {
        "armmode": "armed_away",
        "configured": true,
        "disarmed_entry_delay": 0,
        "disarmed_exit_delay": 0,
        "armed_away_entry_delay": 120,
        "armed_away_exit_delay": 120,
        "armed_away_trigger_duration": 120,
        "armed_stay_entry_delay": 120,
        "armed_stay_exit_delay": 120,
        "armed_stay_trigger_duration": 120,
        "armed_night_entry_delay": 120,
        "armed_night_exit_delay": 120,
        "armed_night_trigger_duration": 120
    },
    "state": {
        "armstate": "armed_away",
        "seconds_remaining": 0
    },
    "devices": {
        "ec:1b:bd:ff:fe:6f:c3:4d-01-0501": {
            "armmask": "none"
        },
        "00:15:8d:00:02:af:95:f9-01-0101": {
            "armmask": "AN",
            "trigger": "state/vibration"
        }
    }
  }
}
</code>
</pre>

#### Response fields

See <a href="#getalarmsystem">Get alarm system</a> for a full description of the attributes.


### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get alarm system<a name="getalarmsystem">&nbsp;</a>

    GET /api/<apikey>/alarmsytems/<id>

Returns all attributes of an alarm system.

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
    "name": "default",
    "config": {
        "armmode": "armed_away",
        "configured": true,
        "disarmed_entry_delay": 0,
        "disarmed_exit_delay": 0,
        "armed_away_entry_delay": 120,
        "armed_away_exit_delay": 120,
        "armed_away_trigger_duration": 120,
        "armed_stay_entry_delay": 120,
        "armed_stay_exit_delay": 120,
        "armed_stay_trigger_duration": 120,
        "armed_night_entry_delay": 120,
        "armed_night_exit_delay": 120,
        "armed_night_trigger_duration": 120
    },
    "state": {
        "armstate": "armed_away",
        "seconds_remaining": 0
    },
    "devices": {
        "ec:1b:bd:ff:fe:6f:c3:4d-01-0501": {
            "armmask": "none"
        },
        "00:15:8d:00:02:af:95:f9-01-0101": {
            "armmask": "AN",
            "trigger": "state/vibration"
        }
    }
}
</code>
</pre>

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The alarm system name.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>config</td>
      <td>Object</td>
      <td>The configuration of the alarm system.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Object</td>
      <td>The current state of the alarm system.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>devices</td>
      <td>Object</td>
      <td>List of devices which are added to the alarm system.</td>
      <td>R</td>
    </tr>
  </tbody>
</table>

##### Config object

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>armmode</td>
      <td>String</td>
      <td>
        <p>The target arm mode.</p>
        <ul class="value-list">
          <li>"disarmed"</li>
          <li>"armed_stay"</li>
          <li>"armed_night"</li>
          <li>"armed_away"</li>
        </ul>
      </td>
      <td>RW</td>
    </tr>
    <tr>
      <td>configured</td>
      <td>Bool</td>
      <td>Is <code>true</code> when a PIN code is configured.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>disarmed_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>disarmed_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_away_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_away_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_away_trigger_duration</td>
      <td>Number (0–255) </td>
      <td>The alarm trigger duration.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_stay_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_stay_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_stay_trigger_duration</td>
      <td>Number (0–255)</td>
      <td>The alarm trigger duration.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_night_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_night_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>RW</td>
    </tr>
    <tr>
      <td>armed_night_trigger_duration</td>
      <td>Number (0–255)</td>
      <td>The alarm trigger duration.</td>
      <td>RW</td>
    </tr>
  </tbody>
</table>

The default values for **entry_delay**, **exit_delay**, and **trigger_duration** are 120 seconds.
Delay options are described in [Entry and exit delays](#entry-and-exit-delays).

##### State object

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>armstate</td>
      <td>String</td>
      <td>
        <p>The current alarm system state, which can be different from the <code>config.armmode</code> during state transitions.</p>
        <ul class="value-list">
          <li>"disarmed"</li>
          <li>"armed_stay"</li>
          <li>"armed_night"</li>
          <li>"armed_away"</li>
          <li>"exit_delay"</li>
          <li>"entry_delay"</li>
          <li>"in_alarm"</li>
          <li>"arming_stay"</li>
          <li>"arming_night"</li>
          <li>"arming_away"</li>
        </ul>
      </td>
      <td>R</td>
    </tr>
	<tr>
      <td>seconds_remaining</td>
      <td>Number (0–255)</td>
      <td>
        <p>
        	During "exit_delay" and "entry_delay" states, this value holds the remaining time. In all other states the value is 0.
    	</p>
      </td>
      <td>R</td>
    </tr>
  </tbody>
</table>

##### Devices object

The keys in the `devices` object refer to the `uniqueid` of a light, sensor, or keypad.

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>armmask</td>
      <td>String</td>
      <td>
        <p>A combination of arm modes in which the device triggers alarms.</p>
        <ul class="value-list">
          <li>A — <code>armed_away</code></li>
          <li>N — <code>armed_night</code></li>
          <li>S — <code>armed_stay</code></li>
          <li>"none" — for keypads and keyfobs</li>
        </ul>
      </td>
      <td>R</td>
    </tr>
     <tr>
      <td>trigger</td>
      <td>String</td>
      <td>
        <p>Specifies arm modes in which the device triggers alarms.</p>
        <ul class="value-list">
          <li>"state/presence"</li>
          <li>"state/open"</li>
          <li>"state/vibration"</li>
          <li>"state/buttonevent"</li>
          <li>"state/on"</li>
        </ul>
        <p>This attribute is not available for keypads and keyfobs.</p>
      </td>
      <td>R</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Set alarm system attributes<a name="setattr">&nbsp;</a>

    PUT /api/<apikey>/alarmsystems/<id>

Sets attributes of an alarm system.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>
      	<p>Name of the alarm system</p>
      	<p>(max. 32 characters)</p>
      </td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data
    {
      "name": "Home alarm system"
    }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "/alarmsystems/1/name": "Home alarm system" } } ]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Set alarm system configuration<a name="updateconfig">&nbsp;</a>

    PUT /api/<apikey>/alarmsystems/<id>/config

This request configures the basic configuration of an alarm system.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>code0</td>
      <td>String</td>
      <td>
      	<p>The main PIN code</p>
      	<p>(4–16 characters)</p>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>disarmed_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>disarmed_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_away_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_away_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_away_trigger_duration</td>
      <td>Number (0–255) </td>
      <td>The alarm trigger duration.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_stay_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_stay_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_stay_trigger_duration</td>
      <td>Number (0–255)</td>
      <td>The alarm trigger duration.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_night_entry_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before an alarm is triggered.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_night_exit_delay</td>
      <td>Number (0–255)</td>
      <td>The delay in seconds before the arm mode is armed.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>armed_night_trigger_duration</td>
      <td>Number (0–255)</td>
      <td>The alarm trigger duration.</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

The PIN code `code0` is verified when a keypad tries to arm or disarm the alarm system. It is also required to change the target `armmode` via REST-API.

!!! Note
    1. Be aware that some keypads might not support long PIN codes.
    2. The PIN code is write-only, it can't be read back.
    3. The PIN code is encrypted with scrypt, and stored in the database

### Example request data
    {
      "code0": "12345"
    }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "/alarmsystems/1/config/configured": true } } ]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Add keypad to alarm system<a name="linkkeypad">&nbsp;</a>

    PUT /api/<apikey>/alarmsystems/<id>/device/<uniqueid>


A keypad can be added to exactly *one* alarm system.

&rarr; After pairing a keypad as sensor, it's automatically added to the default alarm system with id "1".

* Keypads use the the alarm system PIN code (see [Update alarm system configuration](#updateconfig)), which is verified each time the keypad arms or disarms the alarm system.
* If a valid PIN code is entered on the keypad, the alarm system's state changes according to the requested arm or disarm command.
* **Important:** For REST-API clients a keypad is a **read-only** sensor. The alarm system automatically takes care of: controlling the keypad's panel state, entry and exit delays, and state transitions.


!!! Note
    The request is the same as [Add device to alarm system](#adddevice) request, but is allowed to have an empty JSON object as body content.

### Parameters

Empty JSON object.

    { }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "added": "/alarmsystems/1/device/ec:1b:bd:ff:fe:6f:c3:4d-01-0501" } } ]
</code>
</pre>

### Sensor resource

Each Keypad is represented by a "ZHAAncillaryControl" `/sensor` resource, which is wired to the alarm system and automatically reflects its state on the keypad panel.

**Example Linkind keypad**

<pre class="headers">
<code class="no-highlight">
GET /api/12345/sensors/ec:1b:bd:ff:fe:6f:c3:4d-01-0501
</code>
</pre>
<pre class="highlight">
<code>
{
    "config": {
        "battery": 95,
        "enrolled": 1,
        "on": true,
        "pending": [],
        "reachable": true
    },
    "ep": 1,
    "etag": "5aaa1c6bae8501f59929539c6e8f44d6",
    "lastseen": "2021-07-25T18:07Z",
    "manufacturername": "lk",
    "modelid": "ZB-KeypadGeneric-D0002",
    "name": "AncillaryControl 41",
    "state": {
        "action": "armed_stay",
        "lastupdated": "2021-07-25T18:02:51.172",
        "lowbattery": false,
        "panel": "exit_delay",
        "seconds_remaining": 55,
        "tampered": false
    },
    "swversion": "3.13",
    "type": "ZHAAncillaryControl",
    "uniqueid": "ec:1b:bd:ff:fe:6f:c3:4d-01-0501"
}
</code>
</pre>

The read-only attribute `state.action` contains the last action a user invoked on the keypad.

<table class="table table-bordered">
  <thead>
    <tr><th><code>state.action</code></th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>disarmed</code></td>
      <td>Sucessful request to <code>disarmed</code> the alarm system.</td>
    </tr>
    <tr>
      <td><code>armed_stay</code></td>
      <td>Sucessful request for <code>armed_stay</code> arm mode.</td>
    </tr>
    <tr>
      <td><code>armed_night</code></td>
      <td>Sucessful request for <code>armed_night</code> arm mode.</td>
    </tr>
    <tr>
      <td><code>armed_away</code></td>
      <td>Sucessful request for <code>armed_away</code> arm mode.</td>
    </tr>
    <tr>
      <td><code>invalid_code</code></td>
      <td>The last entered PIN code was invalid.</td>
    </tr>
    <tr>
      <td><code>panic</code></td>
      <td>The panic or SOS alarm was triggered.</td>
    </tr>
    <tr>
      <td><code>emergency</code></td>
      <td>The emergency alarm was triggert.</td>
    </tr>
    <tr>
      <td><code>fire</code></td>
      <td>The fire alarm was triggered.</td>
    </tr>
  </tbody>
</table>

When a keypad requests a new arm mode it is not set immediately, first the state machine transitions through various states with exit and entry delays.

-------------------------------

The read-only attribute `state.panel` represents the state machine and mirrors the alarm system `state.armstate` attribute.
It reflects what is shown on the panel (when activated by the keypad's proximity sensor).

Note that due its shared nature, the attribute can also be controlled by other keypads, and by arming and disarming the alarm system via REST-API request.


<table class="table table-bordered">
  <thead>
    <tr><th><code>state.panel</code></th><th>Effect on the keypad panel</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><code>disarmed</code></td>
      <td rowspan="4">
        Armed and disarmed states are indicated with the respective symbol's LED and one audio beep.
      </td>
    </tr>
    <tr>
      <td><code>armed_stay</code></td>
      <td style="display: none;"></td>
    </tr>
    <tr>
      <td><code>armed_night</code></td>
      <td style="display: none;"></td>
    </tr>
    <tr>
      <td><code>armed_away</code></td>
      <td style="display: none;"></td>
    </tr>
    <tr>
      <td><code>exit_delay</code></td>
      <td rowspan="2">
        Exit and entry delays are indicated by flashing a symbol's LED and multiple audio beeps.
        During these states the <code>seconds_remaining</code> attribute holds the remaining time until the next state is reached.
      </td>
    </tr>
    <tr>
      <td><code>entry_delay</code></td>
      <td style="display: none;"></td>
    </tr>
    <tr>
      <td><code>not_ready</code></td>
      <td>Error conditions or undefined states, are signaled by audio or flashing a symbol's LED.</td>
    </tr>
    <tr>
      <td><code>in_alarm</code></td>
      <td >The alarm state is indicated by intense audio beeps, or a neutral setting if not supported.</td>
    </tr>
    <tr>
      <td><code>arming_stay</code></td>
      <td rowspan="3" style="border-bottom: none !important;">
        The arming states are set after the <code>exit_delay</code> state, and before the respective armed state. Like the delay states, they are indicated by multiple audio beeps and flashing a symbol's LED.
      </td>
    </tr>
    <tr>
      <td><code>arming_night</code></td>
      <td style="display: none;"></td>
    </tr>
    <tr>
      <td><code>arming_away</code></td>
      <td style="display: none;"></td>
    </tr>
  </tbody>
</table>

!!! Note
    The `state.panel` attribute is read-only and managed automatically by the alarm system.

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Add device to alarm system<a name="adddevice">&nbsp;</a>

    PUT /api/<apikey>/alarmsystems/<id>/device/<uniqueid>

A device can be linked to exactly *one* alarm system. If it is added to another alarm system, it is automatically removed from the prior one.

This request is used for adding and also for updating a device entry.

The `uniqueid` refers to sensors, lights, or keypads. Adding a light can be useful, e.g. when an alarm should be triggered, after a light is powered or switched on in the basement.

### Example request data
<pre class="headers">
<code class="no-highlight">
PUT /api/12345/alarmsystems/1/device/00:15:8d:00:02:af:95:f9-01-0101
</code>
</pre>
<pre class="highlight">
<code>
{
    "armmask": "AN",
    "trigger": "state/vibration"
}
</code>
</pre>

### Parameters

!!! Note
    For keypads and keyfobs the request body can be an empty object.

        { }

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>armmask</td>
      <td>String</td>
      <td>
      	<p>A combination of arm modes in which the device triggers alarms.</p>
        <ul class="value-list">
          <li>A — <code>armed_away</code></li>
          <li>N — <code>armed_night</code></li>
          <li>S — <code>armed_stay</code></li>
        </ul>
      </td>
      <td>required</td>
    </tr>
     <tr>
      <td>trigger</td>
      <td>String</td>
      <td>
        <p>Specifies what attribute of a device triggers alarms.</p>
        <ul class="value-list">
          <li>"state/presence"</li>
          <li>"state/open"</li>
          <li>"state/vibration"</li>
          <li>"state/buttonevent"</li>
          <li>"state/on"</li>
          <li>"state/action"</li>
        </ul>
        <ul>
          <li>If the parameter is ommited, the default value for the device is selected.</li>
          <li>The "state/action" refers to the "emergency", "fire", and "panic" buttons of a keypad.</li>
        </ul>
      </td>
      <td>optional</td>
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
[ { "success": { "added": "/alarmsystems/1/device/00:15:8d:00:02:af:95:f9-01-0101" } } ]
</code>
</pre>

------------------------------------------------------

## Remove device from alarm system<a name="rmdevice">&nbsp;</a>

    DELETE /api/<apikey>/alarmsystems/<id>/device/<uniqueid>

Removes a device from an alarm system. Note that the respective sensor or light resource is not deleted, only the link to  the alarm system.

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
[ { "success": { "removed": "/alarmsystems/1/device/00:15:8d:00:02:af:95:f9-01-0101" } } ]
</code>
</pre>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Trigger alarm via REST-API<a name="triggeralarm">&nbsp;</a>

<mark>TODO</mark>

------------------------------------------------------

## Arm and disarm via REST-API<a name="armdisarm">&nbsp;</a>

<mark>TODO</mark>

