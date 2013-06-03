---
layout: page
title: Scenes
nav: endpoints
anchors:
  - title: Create scene
    url: "#create"
  - title: Get all scenes
    url: "#getall"
  - title: Get scene attributes
    url: "#getattr"
  - title: Set scene attributes
    url: "#setattr"
  - title: Set scene state
    url: "#setstate"
  - title: Delete scene
    url: "#delete"
---

Scenes provide a easy and performant way to recall often used states to a group.

------------------------------------------------------

## Create scene<a name="create">&nbsp;</a>

    POST /api/<apikey>/groups/<group_id>/scene

Creates a new scene for a group.
The actual state of each light will become the lights scene state.

`Note` Lights which are not reachable (turned off) won't be part of the scene!

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the new group</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data
    { "name": "Garage" }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "3" } } ];
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
      <td>The unique identifier of the group.</td>
    </tr>
  </tbody>
</table>

`Note` creating a group with a name which already exists will not create a new group or fail. Such a call does only return the id of the existing group.

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get all groups<a name="getall">&nbsp;</a>

    GET /api/<apikey>/groups

Returns a list of all groups.

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
        "name": "Living Room"
    },
    "2": {
        "etag": "030cf8c1c0025420f3a0659afab251f5",
        "name": "Kitchen"
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
      <td>Name of a group.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../polling#etag">etag</a> which changes on any action to the group.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get group attributes<a name="getattr">&nbsp;</a>

    GET /api/<apikey>/groups/<id>

Returns the full state of a group.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 0b32030b31ef30a4446c9adff6a6f9e5
Last-Modified: Tue, 15 Nov 2012 10:12:00 GMT
</code>
</pre>
<pre class="highlight">
<code>
{
    "action": {
        "bri": 0,
        "ct": 500,
        "effect": "none",
        "hue": 0,
        "on": false,
        "sat": 0,
        "xy": [ 0, 0 ]
    },
    "etag": "0b32030b31ef30a4446c9adff6a6f9e5",
    "id": "32772",
    "lights": [ "42" ],
    "name": "Livingroom",
    "scenes": [
        { "id": "1", "name": "warmlight" }
    ]
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
      <td>HTTP <a href="../polling#etag">etag</a> which changes on any action to the group.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of the group.</td>
    </tr>
    <tr>
      <td>action</td>
      <td>Object</td>
      <td>The last action which was send to the group.</td>
    </tr>
    <tr>
      <td>action.on</td>
      <td>Bool</td>
      <td>true if the group was turned on.</td>
    </tr>
    <tr>
      <td>action.bri</td>
      <td>Number (0..255)</td>
      <td>Brightness of the group. Depending on the lights 0 might not mean visible "off" but minimum brightness.</td>
    </tr>
    <tr>
      <td>action.hue</td>
      <td>Number (0..65535)</td>
      <td>The hue parameter in the HSV color model is between 0°-360° and is mapped to 0..65535 to get 16-bit resolution.</td>
    </tr>
    <tr>
      <td>action.sat</td>
      <td>Number (0..255)</td>
      <td>Color saturation there 0 means no color at all and 255 is the greatest saturation of the color.</td>
    </tr>
    <tr>
      <td>action.ct</td>
      <td>Number (153..500)</td>
      <td>Mired color temperature. (2000K - 6500K)</td>
    </tr>
    <tr>
      <td>action.xy</td>
      <td>Array</td>
      <td>CIE xy color space coordinates as array [x, y] of real values (0..1).</td>
    </tr>
    <tr>
      <td>action.effect</td>
      <td>String</td>
      <td>Dynamic effect:
        <ul>
          <li>none - no effect</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Set group attributes<a name="setattr">&nbsp;</a>

    PUT /api/<apikey>/groups/<id>

Sets attributes of a group which are not related to its state.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the group</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>lights</td>
      <td>Array</td>
      <td>IDs of the lights which are members of the group.</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data
    {
        "name": "Living Room",
        "lights": [ "1", "4" ]
    }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[
    { "success": { "/groups/1/name": "Living Room" } },
    { "success": { "/groups/1/lights": [ "1", "4" ] } }
];
</code>
</pre>

`Note` In order to add or remove lights to the group the lights must be powered on.

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Set group state<a name="setstate">&nbsp;</a>

    PUT /api/<apikey>/lights/<id>/action

Sets the state of a group.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>on</td>
      <td>Bool</td>
      <td>Set to true to turn the lights on, false to turn them off.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>bri</td>
      <td>Number (0..255)</td>
      <td>Set the brightness of the group. Depending on the lights 0 might not mean visible "off" but minimum brightness. If the lights are off and the value is greater 0 a on=true shall also be provided.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>hue</td>
      <td>Number (0..65535)</td>
      <td>Set the color hue of the group. The hue parameter in the HSV color model is between 0°-360° and is mapped to 0..65535 to get 16-bit resolution.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sat</td>
      <td>Number (0..255)</td>
      <td>Set the color saturation of the group. There 0 means no color at all and 255 is the greatest saturation of the color.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>ct</td>
      <td>Number (153..500)</td>
      <td>Set the Mired color temperature of the group. (2000K - 6500K)</td>
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
          <li>none - lights are not performing a alert</li>
          <li>select - lights are blinking a short time</li>
          <li>lselect - lights are blinking a longer time</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>effect</td>
      <td>String</td>
      <td>Trigger a effect of the group:
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
    { "success": { "/groups/1/action/on": true   }},
    { "success": { "/groups/1/action/bri": 180   }},
    { "success": { "/groups/1/action/hue": 43680 }},
    { "success": { "/groups/1/action/sat": 255   }}
]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Delete group<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/groups/<id>

Deletes a group.

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
[ { "success": { "id": "1" } } ]
</code>
</pre>

`Note` In order to delete the group and therefore remove all lights from the group the lights must be powered on.

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)