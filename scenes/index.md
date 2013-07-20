---
layout: page
title: Scenes
nav: endpoints
order: 4
anchors:
  - title: Create scene
    url: "#create"
  - title: Get all scenes
    url: "#getall"
  - title: Get scene attributes
    url: "#getattr"
  - title: Set scene attributes
    url: "#setattr"
  - title: Store scene
    url: "#store"
  - title: Recall scene
    url: "#recall"
  - title: Delete scene
    url: "#delete"
---

{% include JB/setup %}

Scenes provide an easy and performant way to recall often used states to a group.

------------------------------------------------------

## Create scene<a name="create">&nbsp;</a>

    POST /api/<apikey>/groups/<group_id>/scenes

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

`Note` Creating a scene with a name which already exists will not create a new scene or fail. Such a call will only return the id of the existing scene and store the current state of all lights.

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

[503 Service Unavailable](/errors#503)

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
        "name": "working"
    },
    "2": {
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
      <td>name</td>
      <td>String</td>
      <td>Name of the scene.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

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
    "name": "reading"
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
      <td>Name of the scene.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

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

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Store scene<a name="store">&nbsp;</a>

    PUT /api/<apikey>/groups/<group_id>/scenes/<scene_id>/store

Stores the current group state in the scene.
The actual state of each light in the group will become the lights scene state.

`Note` Lights which are not reachable (turned off) won't be affected!

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

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

[503 Service Unavailable](/errors#503)

------------------------------------------------------

## Recall scene<a name="recall">&nbsp;</a>

    PUT /api/<apikey>/groups/<group_id>/scenes/<scene_id>/recall

Recalls a scene.
The actual state of each light in the group will become the lights scene state stored in each light.

`Note` Lights which are not reachable (turned off) won't be affected!

`Note` In the current API version the state of the lights in the gateway will not be updated directly after recalling a scene. For performance reasons this will happen after some delay.

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

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

[503 Service Unavailable](/errors#503)

------------------------------------------------------

## Delete scene<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/groups/<group_id>/scenes/<scene_id>

Deletes a scene.

`Note` The scene will not be removed from lights which are not reachable (turned off)!

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

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

[503 Service Unavailable](/errors#503)
