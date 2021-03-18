---
title: Groups

---

# Groups

Groups are useful to control many lights at once and provide the base to use scenes.


## Create group<a name="create">&nbsp;</a>

    POST /api/<apikey>/groups

Creates a new empty group.

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
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "3" } } ]
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

!!! note
    Creating a group with a name which already exists will not create a new group or fail. Such a call does only return the id of the existing group.

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get all groups<a name="getall">&nbsp;</a>

    GET /api/<apikey>/groups

Returns a list of all groups.

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
        "devicemembership": [],
        "etag": "ab5272cfe11339202929259af22252ae",
        "hidden" : false,
        "name": "Living Room"
    },
    "2": {
        "devicemembership": ["3"],
        "etag": "030cf8c1c0025420f3a0659afab251f5",
        "hidden" : false,
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
      <td>devicemembership</td>
      <td>Array</td>
      <td>If this group was created by a device (switch or sensor) this list contains the device ids.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of a group.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../../misc/polling#etag">etag</a> which changes on any action to the group.</td>
    </tr>
	<tr>
      <td>hidden</td>
      <td>Bool</td>
      <td>Indicates if this group is hidden.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get group attributes<a name="getattr">&nbsp;</a>

    GET /api/<apikey>/groups/<id>

Returns the full state of a group.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "0b32030b31ef30a4446c9adff6a6f9e5"
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
    "devicemembership": [],
    "etag": "0b32030b31ef30a4446c9adff6a6f9e5",
    "hidden": false,
    "id": "32772",
    "lights": [ "3","42","43" ],
    "lightsequence": [ "42","43","3" ],
    "multideviceids": ["2"],
    "name": "Livingroom",
    "scenes": [
        { "id": "1", "name": "warmlight" }
    ],
    "state": 0
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
      <td>Number (0&ndash;255)</td>
      <td>Brightness of the group. Depending on the lights 0 might not mean visible "off" but minimum brightness.</td>
    </tr>
    <tr>
      <td>action.hue</td>
      <td>Number (0&ndash;65535)</td>
      <td>The hue parameter in the HSV color model is between 0°&ndash;360° and is mapped to 0&ndash;65535 to get 16-bit resolution.</td>
    </tr>
    <tr>
      <td>action.sat</td>
      <td>Number (0&ndash;255)</td>
      <td>Color saturation there 0 means no color at all and 255 is the greatest saturation of the color.</td>
    </tr>
    <tr>
      <td>action.ct</td>
      <td>Number (153&ndash;500)</td>
      <td>Mired color temperature. (2000K&ndash;6500K)</td>
    </tr>
    <tr>
      <td>action.xy</td>
      <td>Array</td>
      <td>CIE xy color space coordinates as array [x, y] of real values (0&ndash;1).</td>
    </tr>
    <tr>
      <td>action.effect</td>
      <td>String</td>
      <td>Dynamic effect:
        <ul>
          <li>none - no effect</li>
          <li>colorloop</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>devicemembership</td>
      <td>Array</td>
      <td>A list of device ids (sensors) if this group was created by a device.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../../misc/polling#etag">etag</a> which changes on any action to the group.</td>
    </tr>
    <tr>
      <td>hidden</td>
      <td>Bool</td>
      <td>Indicates the hidden status of the group. Has no effect at the gateway but apps can uses this to hide groups.</td>
    </tr>
    <tr>
      <td>id</td>
      <td>String</td>
      <td>The id of the group.</td>
    </tr>
    <tr>
      <td>lights</td>
      <td>Array</td>
      <td>A list of all light ids of this group. Sequence is defined by the gateway.</td>
    </tr>
    <tr>
      <td>lightsequence</td>
      <td>Array</td>
      <td>A list of light ids of this group that can be sorted by the user. Need not to contain all light ids of this group.</td>
    </tr>
    <tr>
      <td>mulitdeviceids</td>
      <td>Array</td>
      <td>A list of light ids of this group that are subsequent ids from multidvices with multiple endpoints like the FLS-PP.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of the group.</td>
    </tr>
    <tr>
      <td>scenes</td>
      <td>Array</td>
      <td>A list of scenes of the group.</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Number</td>
      <td>Deprecated - will be removed in future.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[304 Not Modified](../../misc/errors#304)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

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
      <td>String (0&ndash;32)</td>
      <td>The name of the group</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>lights</td>
      <td>Array</td>
      <td>IDs of the lights which are members of the group.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>hidden</td>
      <td>Bool</td>
      <td>Indicates the hidden status of the group. Has no effect at the gateway but apps can uses this to hide groups.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>lightsequence</td>
      <td>Array</td>
      <td>Specify a sorted list of light ids that can be used in apps.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>mulitdeviceids</td>
      <td>Array</td>
      <td>Append the subsequential light ids of multidevices like the FLS-PP if the app should handle that light differently.</td>
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
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "000bf36b51ef3324446c98hdf6a6ace6"
</code>
</pre>
<pre class="highlight">
<code>
[
    { "success": { "/groups/1/name": "Living Room" } },
    { "success": { "/groups/1/lights": [ "1", "4" ] } }
]
</code>
</pre>

!!! note
    In order to add or remove lights to the group the lights must be powered on.

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Set group state<a name="setstate">&nbsp;</a>

    PUT /api/<apikey>/groups/<id>/action

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
      <td>toggle</td>
      <td>Bool</td>
      <td>Set to true toggles the lights of that group from on to off or vice versa, false has no effect. **Notice:** This setting supersedes the `on` parameter!</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>bri</td>
      <td>Number (0&ndash;255)</td>
      <td>Set the brightness of the group. Depending on the lights 0 might not mean visible "off" but minimum brightness. If the lights are off and the value is greater 0 a on=true shall also be provided.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>hue</td>
      <td>Number (0&ndash;65535)</td>
      <td>Set the color hue of the group. The hue parameter in the HSV color model is between 0°&ndash;360° and is mapped to 0&ndash;65535 to get 16-bit resolution.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>sat</td>
      <td>Number (0&ndash;255)</td>
      <td>Set the color saturation of the group. There 0 means no color at all and 255 is the highest saturation of the color.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>ct</td>
      <td>Number (153&ndash;500)</td>
      <td>Set the Mired color temperature of the group. (2000K&ndash;6500K)</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>xy</td>
      <td>Array</td>
      <td>Set the CIE xy color space coordinates as array [x, y] of real values (0&ndash;1).</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>alert</td>
      <td>String</td>
      <td>Trigger a temporary alert effect:
        <ul>
          <li>none - lights are not performing an alert</li>
          <li>select - lights are blinking a short time</li>
          <li>lselect - lights are blinking a longer time</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>effect</td>
      <td>String</td>
      <td>Trigger an effect of the group:
        <ul>
          <li>none - no effect</li>
          <li>colorloop - the lights of the group will cycle continously through all colors with the speed specified by colorloopspeed</li>
        </ul>
      </td>
      <td>optional</td>
    </tr>
    <tr>
      <td>colorloopspeed</td>
      <td>Number (1&ndash;255)</td>
      <td>Specifies the speed of a colorloop. 1 = very fast, 255 = very slow (default: 15). This parameter only has an effect when it is called together with effect colorloop.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>transitiontime</td>
      <td>Number</td>
      <td>Transition time in 1/10 seconds between two states. Note that not all states support a transition time. For example, a transition time when setting <pre>on</pre> will be ignored as the Zigbee On and Off commands do not support transition times. In general, light attributes that support a range of values support transition times, while boolean values do not.</td>
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
    { "success": { "/groups/1/action/on": true   }},
    { "success": { "/groups/1/action/bri": 180   }},
    { "success": { "/groups/1/action/hue": 43680 }},
    { "success": { "/groups/1/action/sat": 255   }}
]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Delete group<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/groups/<id>

Deletes a group.

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
[ { "success": { "id": "1" } } ]
</code>
</pre>

!!! note
    In order to delete the group and therefore remove all lights from the group the lights must be powered on.

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)
