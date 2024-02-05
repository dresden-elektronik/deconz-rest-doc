---
title: Lights
---

# Lights

Monitor and control single lights.


## Get all lights<a name="getall">&nbsp;</a>

    GET /api/<apikey>/lights

Returns a list of all lights.

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
        "etag": "026bcfe544ad76c7534e5ca8ed39047c",
        "hascolor": true,
        "manufacturername": "dresden elektronik",
        "modelid": "FLS-PP3",
        "name": "Light 1",
        "pointsymbol": {},
        "state": {
            "alert": "none",
            "bri": 111,
            "colormode": "ct",
            "ct": 307,
            "effect": "none",
            "hue": 7998,
            "on": false,
            "reachable": true,
            "sat": 172,
            "xy": [ 0.421253, 0.39921 ]
        },
        "swversion": "020C.201000A0",
        "type": "Extended color light",
        "uniqueid": "00:21:2E:FF:FF:00:73:9F-0A"
    },

    "2": {
        "etag": "026bcfe544ad76c7534e5ca8ed39047c",
        "hascolor": false,
        "manufacturername": "dresden elektronik",
        "modelid": "FLS-PP3 White",
        "name": "Light 2",
        "pointsymbol": {},
        "state": {
            "alert": "none",
            "bri": 1,
            "effect": "none",
            "on": false,
            "reachable": true
        },
        "swversion": "020C.201000A0",
        "type": "Dimmable light",
        "uniqueid": "00:21:2E:FF:FF:00:73:9F-0B"
    }
}
</code>
</pre>

#### Response fields

The whole light object as descripted in [Get light state](#getstate).

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get light state<a name="getstate">&nbsp;</a>

    GET /api/<apikey>/lights/<id>

Returns the full state of a light.

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
        "etag": "026bcfe544ad76c7534e5ca8ed39047c",
        "hascolor": true,
        "manufacturername": "dresden elektronik",
        "modelid": "FLS-PP3",
        "name": "Light 1",
        "pointsymbol": {},
        "state": {
            "alert": "none",
            "bri": 111,
            "colormode": "ct",
            "ct": 307,
            "effect": "none",
            "hue": 7998,
            "on": false,
            "reachable": true,
            "sat": 172,
            "xy": [ 0.421253, 0.39921 ]
        },
        "swversion": "020C.201000A0",
        "type": "Extended color light",
        "uniqueid": "00:21:2E:FF:FF:00:73:9F-0A"
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
      <td>colorcapabilities</td>
      <td>Number</td>
      <td>The color capabilities as reported by the light.</td>
    </tr>
    <tr>
      <td>ctmax</td>
      <td>Number</td>
      <td>The maximum mired color temperature value a device supports.</td>
    </tr>
    <tr>
      <td>ctmin</td>
      <td>Number</td>
      <td>The minimum mired color temperature value a device supports.</td>
    </tr>
    <tr>
      <td>lastannounced</td>
      <td>String</td>
      <td>Last time the device announced itself to the network.</td>
    </tr>
    <tr>
      <td>lastseen</td>
      <td>String</td>
      <td>Last time the device has transmitted any data.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../../misc/polling#etag">etag</a> which changes on any action to the light.</td>
    </tr>
    <tr>
      <td>hascolor</td>
      <td>bool</td>
      <td>Indicates if the light can change color. Deprecated - use state instead: if light has no color colormode, hue and xy will not be shown.</td>
    </tr>
    <tr>
      <td>manufacturername</td>
      <td>String</td>
      <td>The manufacturer name of the light device.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of a light.</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>String</td>
      <td>An identifier unique to the product.</td>
    </tr>
    <tr>
      <td>pointsymbol</td>
      <td>Object</td>
      <td>Not used in the current version.</td>
    </tr>
    <tr>
      <td>powerup</td>
      <td>Number</td>
      <td>SETTABLE. Brightness to set after power on (limited to DE devices).</td>
    </tr>
    <tr>
      <td>swversion</td>
      <td>String</td>
      <td>Firmware version.</td>
    </tr>
    <tr>
      <td>type</td>
      <td>String</td>
      <td>Human readable type of the light.</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Object</td>
      <td>The current state of the light.</td>
    </tr>
    <tr>
      <td>state.on</td>
      <td>Bool</td>
      <td>true if the light is on.</td>
    </tr>
    <tr>
      <td>state.bri</td>
      <td>Number (0&ndash;255)</td>
      <td>Brightness of the light. Depending on the light type 0 might not mean visible "off" but minimum brightness.</td>
    </tr>
    <tr>
      <td>state.effect</td>
      <td>String</td>
      <td>Run special effect (if supported). See the device documentation for all possible values.</td>
    </tr>
    <tr>
      <td>state.hue</td>
      <td>Number (0&ndash;65535)</td>
      <td>Color hue of the light. The hue parameter in the HSV color model is between 0°&ndash;360° and is mapped to 0&ndash;65535 to get 16-bit resolution.</td>
    </tr>
    <tr>
      <td>state.sat</td>
      <td>Number (0&ndash;255)</td>
      <td>Color saturation of the light. There 0 means no color at all and 255 is the greatest saturation of the color.</td>
    </tr>
    <tr>
      <td>state.ct</td>
      <td>Number (ctmin&ndash;ctmax)</td>
      <td>
        Mired color temperature of the light.</br>
        Where Mired is 1000000 / color temperature (in kelvins).
      </td>
    </tr>
    <tr>
      <td>state.xy</td>
      <td>Array</td>
      <td>CIE xy color space coordinates as array [x, y] of real values (0&ndash;1).</td>
    </tr>
    <tr>
      <td>state.alert</td>
      <td>String</td>
      <td>
        <p>Temporary alert effect.</p>
        <ul class="value-list">
          <li>"none" &mdash; light is not performing an alert</li>
          <li>"select" &mdash; light is blinking a short time</li>
          <li>"lselect" &mdash; light is blinking a longer time</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.colormode</td>
      <td>String</td>
      <td>
        <p>The current color mode of the light:</p>
        <ul class="value-list">
          <li>"hs" &mdash; hue and saturation</li>
          <li>"xy" &mdash; CIE xy values</li>
          <li>"ct" &mdash; color temperature</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.effect</td>
      <td>String</td>
      <td>
        <p>Effect of the light:</p>
        <ul class="value-list">
          <li>"none" &mdash; no effect</li>
          <li>"colorloop" &mdash; cycle through hue values 0&ndash;360</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.speed</td>
      <td>Number (0&ndash;6)</td>
      <td>SETTABLE. Sets the speed of fans/ventilators.</td>
    </tr>
    <tr>
      <td>state.reachable</td>
      <td>Bool</td>
      <td>true if the light is reachable and accepts commands.</td>
    </tr>
    <tr>
      <td>uniqueid</td>
      <td>String</td>
      <td>The unique id of the light. It consists of the MAC address of the light followed by a dash and an unique endpoint identifier in the range 01 to FF.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[304 Not Modified](../../misc/errors#304)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Set light state<a name="setstate">&nbsp;</a>

    PUT /api/<apikey>/lights/<id>/state

Sets the state of a light.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>alert</td>
      <td>String</td>
      <td>
        <p>Trigger a temporary alert effect:</p>
        <ul class="value-list">
          <li>"none" &mdash; light is not performing an alert</li>
          <li>"select" &mdash; light is blinking a short time</li>
          <li>"lselect" &mdash; light is blinking a longer time</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>bri</td>
      <td>Number (0&ndash;255)</td>
      <td>Set the brightness of the light. Depending on the light type 0 might not mean visible "off" but minimum brightness. If the light is off and the value is greater 0 a on=true shall also be provided.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>colorloopspeed</td>
      <td>Number (1&ndash;255)</td>
      <td>
        <p>Specifies the speed of a colorloop (default: 15).</p>
        <ul class="value-list">
          <li>1 = very fast</li>
          <li>255 = very slow</li>
        </ul>
        <p>This parameter only has an effect when it is called together with effect colorloop.</p>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>ct</td>
      <td>Number (ctmin&ndash;ctmax)</td>
      <td>
        Set the Mired color temperature of the light.</br>
        Where Mired is 1000000 / color temperature (in kelvins).
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>effect</td>
      <td>String</td>
      <td>
        <p>Trigger an effect of the light:</p>
        <ul class="value-list">
          <li>"none" &mdash; no effect</li>
          <li>"colorloop" &mdash; the light will cycle continously through all colors with the speed specified by colorloopspeed</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>hue</td>
      <td>Number (0&ndash;65535)</td>
      <td>Set the color hue of the light. The hue parameter in the HSV color model is between 0°&ndash;360° and is mapped to 0&ndash;65535 to get 16-bit resolution.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>Set to true to turn the light on, false to turn it off.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sat</td>
      <td>Number (0&ndash;255)</td>
      <td>Set the color saturation of the light. There 0 means no color at all and 255 is the greatest saturation of the color.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>transitiontime</td>
      <td>Number</td>
      <td>Transition time in 1/10 seconds between two states. Note that not all states support a transition time. For example, a transition time when setting <pre>on</pre> will be ignored as the Zigbee On and Off commands do not support transition times. In general, light attributes that support a range of values support transition times, while boolean values do not.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>xy</td>
      <td>Array</td>
      <td>Set the CIE xy color space coordinates as array [x, y] of real values (0&ndash;1).</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

#### Window covering parameters

For historic reasons window covering devices are currently exposed under the lights endpoint.

<p>For lights with <b>type</b>:</p>
<ul  class="value-list">
  <li>"Window covering controller"</li>
  <li>"Window covering device"</li>
</ul>

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>open</td>
      <td>Bool</td>
      <td>Set to true to lift the shutter to 0&thinsp;%, false to lift it to 100&thinsp;%.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>stop</td>
      <td>Bool</td>
      <td>Stops the current action.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>lift</td>
      <td>Number<br/>String</td>
      <td>
        <p>Supported range is 0&ndash;100 or special value "stop".</p>
        <p><code class="api-attribute">lift</code> is best understood as “percentage closed”. So for any lift value below 100&thinsp;%, open is true.</p>
        <ul  class="value-list">
          <li>0&ndash;99 &mdash; <code class="api-attribute">open</code> is true</li>
          <li>100 &mdash; <code class="api-attribute">open</code> is false</li>
          <li>"stop" &mdash; Stops the lift action</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>tilt</td>
      <td>Number</td>
      <td>Sets the tilt angle of the shutter (0&ndash;100&thinsp;%).</td>
      <td>optional</td>
    </tr>
    <tr>
      <td colspan="4">
        <b>Deprecated</b>
      </td>
    </tr>
    <tr>
      <td>bri</td>
      <td>Number String</td>
      <td>
        <p>(deprecated by "lift")</p>
        0&ndash;255 or "stop"
        where <code class="api-attribute">lift</code> = bri * 100 / 254.
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>bri_inc</td>
      <td>Number</td>
      <td>
        <p>(deprecated by "stop")</p>
        Only supported value is 0 meaning stop.
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>
        <p>(deprecated by "open")</p>
        <p>true when lift > 0</p>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sat</td>
      <td>Number</td>
      <td>
        <p>(deprecated by "tilt")</p>
        0&ndash;255 where <code class="api-attribute">tilt</code> = sat * 100 / 254.
      </td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data
    {
      "on": true,
      "bri": 180,
      "hue": 43680,
      "sat": 255,
      "transitiontime": 10
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
[
    { "success": { "/lights/1/state/on": true   }},
    { "success": { "/lights/1/state/bri": 180   }},
    { "success": { "/lights/1/state/hue": 43680 }},
    { "success": { "/lights/1/state/sat": 255   }}
]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Set light attributes<a name="setattr">&nbsp;</a>

    PUT /api/<apikey>/lights/<id>

Sets attributes of a light which are not related to its state.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String (0&ndash;32)</td>
      <td>Set the name of the light.</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data
    { "name": "Living Room 1" }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[{ "success": { "/lights/1/name": "Living Room 1"}}]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Delete light<a name="deletelight">&nbsp;</a>

    DELETE /api/<apikey>/lights/<id>

Removes the light from the gateway. It will not be shown in any REST-API call. Also deletes all groups and scenes on the light device.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>reset</td>
      <td>Bool</td>
      <td>If true sends a network leave command to the light device (may not supported by each manufacturer).</td>
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
[{ "success": { "id": "1"}}]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Remove from all groups<a name="removegroups">&nbsp;</a>

    DELETE /api/<apikey>/lights/<id>/groups

Remove the light from all groups it is a member of.

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[{ "success": { "id": "1"}}]
</code>
</pre>

### Possible errors

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Remove from all scenes<a name="removescenes">&nbsp;</a>

    DELETE /api/<apikey>/lights/<id>/scenes

Remove the light from all scenes it is a member of.

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[{ "success": { "id": "1"}}]
</code>
</pre>

### Possible errors

[404 Not Found](../../misc/errors#404)
