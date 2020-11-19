---
title: Scenes
---

# Scenes

Scenes provide an easy and performant way to recall often used states to a group.

## Create scene<a name="create">&nbsp;</a>

    POST /api/<apikey>/groups/<group_id>/scenes

Creates a new scene for a group.
The actual state of each light will become the lights scene state.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the new scene</td>
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
      <td>The unique identifier of the scene.</td>
    </tr>
  </tbody>
</table>

!!! note
    Creating a scene with a name which already exists will not create a new scene or fail. Such a call will only return the id of the existing scene and store the current state of all lights.

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Get all scenes<a name="getall">&nbsp;</a>

    GET /api/<apikey>/groups/<group_id>/scenes

Returns a list of all scenes of a group.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 203941fel3ds8ad61903224
</code>
</pre>
<pre class="highlight">
<code>
{
    "1": {
        "lights": ["1","2"],
        "name": "working"
    },
    "2": {
        "lights": ["3"],
        "name": "reading"
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
      <td>lights</td>
      <td>Array</td>
      <td>Lights which are members of the scene.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of the scene.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Get scene attributes<a name="getattr">&nbsp;</a>

    GET /api/<apikey>/groups/<group_id>/scenes/<scene_id>

Returns all attributes of a scene.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 0b32030b31ef30a4446c9adff6a6f9e5
</code>
</pre>
<pre class="highlight">
<code>
{
    lights": [
        {
            "bri": 111
            "id": "3"
            "on": false
            "transitiontime": 0
            "x": 27499
            "y": 26060
        }
    ],
    "name": "reading"
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
      <td>lights</td>
      <td>Array</td>
      <td>Contains objects which describe the state fof each light in the scene.
      </td>
    </tr>
    <tr>
      <td>lights[].id</td>
      <td>String</td>
      <td>The id of the light.</td>
    </tr>
    <tr>
      <td>lights[].on</td>
      <td>Bool</td>
      <td>True if the light is on.</td>
    </tr>
    <tr>
      <td>lights[].bri</td>
      <td>Number (0..255)</td>
      <td>The brightness of the light.</td>
    </tr>
    <tr>
      <td>lights[].transitiontime</td>
      <td>Number</td>
      <td>The scene fading transition time in 1/10 seconds.</td>
    </tr>
    <tr>
      <td>lights[].x</td>
      <td>Number (0..1)</td>
      <td>The color x value of the light.</td>
    </tr>
    <tr>
      <td>lights[].y</td>
      <td>Number (0..1)</td>
      <td>The color y value of the light.</td>
    </tr>
    <tr>
      <td>lights[].ct</td>
      <td>Number</td>
      <td>The mired color temperature value of the light.</td>
    </tr>
    <tr>
      <td>lights[].hue</td>
      <td>Number (0.65535)</td>
      <td>The hue value of the light.</td>
    </tr>
    <tr>
      <td>lights[].sat</td>
      <td>Number (0.255)</td>
      <td>The saturation value of the light.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of the scene.</td>
    </tr>
    <tr>
      <td>state</td>
      <td>Number</td>
      <td>Deprecated - will be removed in future.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Set scene attributes<a name="setattr">&nbsp;</a>

    PUT /api/<apikey>/groups/<group_id>/scenes/<scene_id>

Sets attributes of a scene.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Name of the scene.</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data
    {
      "name": "working"
    }

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
Etag: 030cf8c1c0025420f3a0659afab251f5
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "/groups/1/scenes/1/name": "working" } } ]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Store scene<a name="store">&nbsp;</a>

    PUT /api/<apikey>/groups/<group_id>/scenes/<scene_id>/store

Stores the current group state in the scene.
The actual state of each light in the group will become the lights scene state.

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
      <td>The unique identifier of the scene.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Recall scene<a name="recall">&nbsp;</a>

    PUT /api/<apikey>/groups/<group_id>/scenes/<scene_id>/recall

Recalls a scene.
The actual state of each light in the group will become the lights scene state stored in each light.

!!! note
    Lights which are not reachable (turned off) won't be affected!

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
      <td>The unique identifier of the scene.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Modify scene<a name="modify">&nbsp;</a>

    PUT /api/<apikey>/groups/<group_id>/scenes/<scene_id>/lights/<light_id>/state

Modifies the state of a light of the scene.

!!! note
    The light must be a member of the scene.

### Example request data
    {
        "bri": 111
        "on": true
        "transitiontime": 10
        "xy": [ 0.44, 0.98 ]
    }

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>bri</td>
      <td>Number (0..255)</td>
      <td>Brightness of the light</td>
      <td>optional</td>
    </tr>
     <tr>
      <td>on</td>
      <td>Bool</td>
      <td>On/off status of the light</td>
      <td>optional</td>
    </tr>
     <tr>
      <td>transitiontime</td>
      <td>Number</td>
      <td>Transitiontime of the light when the scene is called in 1/10 seconds</td>
      <td>optional</td>
    </tr>
     <tr>
      <td>xy</td>
      <td>Array</td>
      <td>Xy color values of the light mapped to [0..1]</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

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


### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Delete scene<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/groups/<group_id>/scenes/<scene_id>

Deletes a scene.

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
      <td>The unique identifier of the scene.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

