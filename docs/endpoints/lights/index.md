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
        "manufacturer": "dresden elektronik",
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
        "manufacturer": "dresden elektronik",
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
        "manufacturer": "dresden elektronik",
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
      <td></td>
    </tr>
    <tr>
      <td>ctmin</td>
      <td>Number</td>
      <td></td>
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
      <td>manufacturer</td>
      <td>String</td>
      <td>The manufacturer of the light device.</td>
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
      <td>Number (0&ndash;7)</td>
      <td>Run special scenes (if supported).</td>
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
      <td>Number (153&ndash;500)</td>
      <td>Mired color temperature of the light. (2000K&ndash;6500K)</td>
    </tr>
    <tr>
      <td>state.xy</td>
      <td>Array</td>
      <td>CIE xy color space coordinates as array [x, y] of real values (0&ndash;1).</td>
    </tr>
    <tr>
      <td>state.alert</td>
      <td>String</td>
      <td>Temporary alert effect. Following values are possible:
        <ul>
          <li>none - light is not performing an alert</li>
          <li>select - light is blinking a short time</li>
          <li>lselect - light is blinking a longer time</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.colormode</td>
      <td>String</td>
      <td>The current color mode of the light:
        <ul>
          <li>hs - hue and saturation</li>
          <li>xy - CIE xy values</li>
          <li>ct - color temperature</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.effect</td>
      <td>String</td>
      <td>Effect of the light:
        <ul>
          <li>none - no effect</li>
          <li>colorloop</li>
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
      <td>Trigger a temporary alert effect:
        <ul>
          <li>none - light is not performing an alert</li>
          <li>select - light is blinking a short time</li>
          <li>lselect - light is blinking a longer time</li>
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
      <td>Specifies the speed of a colorloop. 1 = very fast, 255 = very slow (default: 15). This parameter only has an effect when it is called together with effect colorloop.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>ct</td>
      <td>Number (153&ndash;500)</td>
      <td>Set the Mired color temperature of the light. (2000K&ndash;6500K)</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>effect</td>
      <td>String</td>
      <td>Trigger an effect of the light:
        <ul>
          <li>none - no effect</li>
          <li>colorloop - the light will cycle continously through all colors with the speed specified by colorloopspeed</li>
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
      <td>Transition time in 1/10 seconds between two states.</td>
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

## Remove all groups<a name="removegroups">&nbsp;</a>

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

## Remove all scenes<a name="removescenes">&nbsp;</a>

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