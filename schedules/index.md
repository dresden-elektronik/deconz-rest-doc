---
layout: page
title: Schedules
nav: endpoints
order: 5
anchors:
  - title: Create schedule
    url: "#create"
  - title: Get all schedules
    url: "#getall"
  - title: Get schedule attributes
    url: "#getattr"
  - title: Set schedule attributes
    url: "#setattr"
  - title: Delete schedule
    url: "#delete"
---

{% include JB/setup %}

Schedules provide the ability to trigger timed commands to groups or lights.

------------------------------------------------------

## Create schedule<a name="create">&nbsp;</a>

    POST /api/<apikey>/schedules

Creates a new schedule.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the new schedule. If the name already exists a number will be appended.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>description</td>
      <td>String</td>
      <td>The description of the schedule.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>command</td>
      <td>Object</td>
      <td>The command to execute when the schedule triggers.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>time</td>
      <td>String</td>
      <td>Time when the schedule shall trigger in UTC ISO 8601:2004 format. The time must be in the future.</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data
    {
        "name": "blue moon",
        "description": "Turns all lights blue",
        "command": {
            "address": "/api/8918fbad2100nag17ca1/groups/5/action",
            "method": "PUT",
            "body": { "on": true, "hue": 43000, "sat": 255 }
        },
        "time": "2013-07-29T09:30:00"
    }

`Note` The address in the command object must contain a valid API key.

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
      <td>The unique identifier of the new schedule.</td>
    </tr>
  </tbody>
</table>

`Note` creating a scene with a name which already exists will not create a new scene or fail. Such a call will only return the id of the existing scene and store the current state of all lights.

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get all schedules<a name="getall">&nbsp;</a>

    GET /api/<apikey>/schedules

Returns a list of all schedules.

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
        "name": "turn all off"
    },
    "2": {
        "name": "morning alarm"
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
      <td>Name of the schedule.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get schedule attributes<a name="getattr">&nbsp;</a>

    GET /api/<apikey>/schedule/<id>

Returns all attributes of a schedule.

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
        "name": "turn all off",
        "description": "Turns all lights off",
        "command": {
            "address": "/api/8918fbad2100nag17ca1/groups/2/action",
            "method": "PUT",
            "body": { "on": false }
        },
        "time": "2013-07-30T20:10:00"
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
      <td>Name of the schedule.</td>
    </tr>
    <tr>
      <td>description</td>
      <td>String</td>
      <td>The description of the schedule.</td>
    </tr>
    <tr>
      <td>command</td>
      <td>Object</td>
      <td>The command to execute when the schedule triggers.</td>
    </tr>
    <tr>
      <td>time</td>
      <td>String</td>
      <td>Time when the schedule shall trigger in UTC ISO 8601:2004 format.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Set schedule attributes <a name="setattr">&nbsp;</a>

    PUT /api/<apikey>/schedules/<id>

Sets attributes of a schedule.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the new schedule. If the name already exists a number will be appended.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>description</td>
      <td>String</td>
      <td>The description of the schedule.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>command</td>
      <td>Object</td>
      <td>The command to execute when the schedule triggers.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>time</td>
      <td>String</td>
      <td>Time when the schedule shall trigger in UTC ISO 8601:2004 format. The time must be in the future.</td>
      <td>required</td>
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
[ { "success": { "/schedules/1/name": "working" } } ]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Delete schedule<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/schedules/<id>

Deletes a schedule.

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
      <td>The unique identifier of the schedule.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)
