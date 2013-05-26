---
layout: page
title: Lights
nav: endpoints
anchors:
  - title: Get all lights
    url: "#getall"
  - title: Get light state
    url: "#getstate"
  - title: Set light state
    url: "#setstate"
  - title: Set light attributes
    url: "#setattr"
  - title: Delete light
    url: "#delete"
  - title: Search lights
    url: "#search"
  - title: Get new lights
    url: "#getnew"
---

Monitor and control single lights.

------------------------------------------------------

## Get all lights<a name="getall">&nbsp;</a>

    GET /api/<apikey>/lights

Returns a list of all lights.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 203941fel3ds8ad61903224
Last-Modified: Tue, 15 Nov 2012 10:12:00 GMT
</code>
</pre>
<pre class="highlight">
<code>
{
    "1": {
        "etag": "ab5272cfe11339202929259af22252ae",
        "name": "FLS-PP"
    },
    "2": {
        "etag": "030cf8c1c0025420f3a0659afab251f5",
        "name": "Hue 1"
    }
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
      <td>name</td>
      <td>String</td>
      <td>Name of a light.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../polling#etag">etag</a> which changes on any action to the light.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get light state<a name="getstate">&nbsp;</a>

    GET /api/<apikey>/lights/<id>

Returns the full state of a light.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 030cf8c1c0025420f3a0659afab251f5
Last-Modified: Tue, 15 Nov 2012 10:12:00 GMT
</code>
</pre>
<pre class="highlight">
<code>
{
    "etag": "030cf8c1c0025420f3a0659afab251f5",
    "name": "FLS-PP",
    "modelid": "FLS-PP-00",
    "pointsymbol": "none",
    "swversion": "00076172",
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

        "nhue": 0.330709,
        "reachable": true,

        "xy": [
            0.805343,
            0.000612754
        ]
    }
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
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../polling#etag">etag</a> which changes on any action to the light.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of a light.</td>
    </tr>
    <tr>
      <td>modelid</td>
      <td>String</td>
      <td>A identifier unique to the product.</td>
    </tr>
    <tr>
      <td>pointsymbol</td>
      <td>String</td>
      <td>Not used in the current version and always set to <em>none</em>.</td>
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
      <td>Number (0..255)</td>
      <td>Brightness of the light. Depending on the light type 0 might not mean visible "off" but minimum brightness.</td>
    </tr>
    <tr>
      <td>state.hue</td>
      <td>Number (0..65535)</td>
      <td>Color hue of the light. The hue parameter in the HSV color model is between 0°-360° and is mapped to 0..65535 to get 16-bit resolution.</td>
    </tr>
    <tr>
      <td>state.sat</td>
      <td>Number (0..255)</td>
      <td>Color saturation of the light. There 0 means no color at all and 255 is the greatest saturation of the color.</td>
    </tr>
    <tr>
      <td>state.ct</td>
      <td>Number (153..500)</td>
      <td>Mired color temperature of the light. (2000K - 6500K)</td>
    </tr>
    <tr>
      <td>state.xy</td>
      <td>Array</td>
      <td>CIE xy color space coordinates as array [x, y] of real values (0..1).</td>
    </tr>
    <tr>
      <td>state.alert</td>
      <td>String</td>
      <td>Temporary alert effect. Following values are possible:
        <ul>
          <li>none - light is not performing a alert</li>
          <li>select - light is blinking a short time</li>
          <li>lselect - light is blinking a longer time</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.colormode</td>
      <td>String</td>
      <td>The current colormode of the light:
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
        </ul>
      </td>
    </tr>
    <tr>
      <td>state.reachable</td>
      <td>Bool</td>
      <td>true if the light is reachable and accepts commands.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

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
      <td>on</td>
      <td>Bool</td>
      <td>Set to true to turn the light on, false to turn it off.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>bri</td>
      <td>Number (0..255)</td>
      <td>Set the brightness of the light. Depending on the light type 0 might not mean visible "off" but minimum brightness. If the light is off and the value is greater 0 a on=true shall also be provided.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>hue</td>
      <td>Number (0..65535)</td>
      <td>Set the color hue of the light. The hue parameter in the HSV color model is between 0°-360° and is mapped to 0..65535 to get 16-bit resolution.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sat</td>
      <td>Number (0..255)</td>
      <td>Set the color saturation of the light. There 0 means no color at all and 255 is the greatest saturation of the color.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>ct</td>
      <td>Number (153..500)</td>
      <td>Set the Mired color temperature of the light. (2000K - 6500K)</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>xy</td>
      <td>Array</td>
      <td>Set the CIE xy color space coordinates as array [x, y] of real values (0..1).</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>alert</td>
      <td>String</td>
      <td>Trigger a temporary alert effect:
        <ul>
          <li>none - light is not performing a alert</li>
          <li>select - light is blinking a short time</li>
          <li>lselect - light is blinking a longer time</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>effect</td>
      <td>String</td>
      <td>Trigger a effect of the light:
        <ul>
          <li>none - no effect</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>transitiontime</td>
      <td>Number</td>
      <td>Transitiontime in 1/10 seconds between two states.</td>
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
<code>
HTTP/1.1 200 OK
Etag: 030cf8c1c0025420f3a0659afab251f5
Last-Modified: Tue, 15 Nov 2012 10:12:00 GMT
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

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

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
      <td>String (0..32)</td>
      <td>Set the name of the light.</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data
    { "name": "Living Room 1" }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 030cf8c1c0025420f3a0659afab251f5
Last-Modified: Tue, 15 Nov 2012 10:12:00 GMT
</code>
</pre>
<pre class="highlight">
<code>
[{ "success": { "/lights/1/name": "Living Room 1"}}]
</code>
</pre>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)