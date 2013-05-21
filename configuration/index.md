---
layout: page
title: Configuration
nav: endpoints
anchors:
  - title: Get configuration
    url: "#getconfig"
  - title: Aquire API key
    url: "#aquireapikey"
  - title: Delete API key
    url: "#deleteapikey"
  - title: Get full state
    url: "#getfullstate"
---

{% include sitepanelnav %}

The configuration endpoint allows to retreive the current configuration of the gateway.

------------------------------------------------------

## Get configuration<a name="getconfig">&nbsp;</a>
	GET /api/<apikey>/config

Returns the current gateway configuration.

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
	"name": "deCONZ GW",
	"ipaddress": "192.168.1.20",
	"mac": "00:15:22:22:00:11:11:a3",
	"linkbutton": false,
	"utc": "2013-05-10T09:01:23",
	"swversion": "0114"
}
</code>
</pre>
#### Fields

<table class="table table-bordered">
	<thead>
		<tr><th>Field</th><th>Type</th><th>Description</th></tr>
	</thead>
	<tbody>
		<tr>
			<td>name</td>
			<td>String</td>
			<td>Name of the gateway.</td>
		</tr>
		<tr>
			<td>ipaddress</td>
			<td>String</td>
			<td>IPv4 address of the gateway.</td>
		</tr>
		<tr>
			<td>mac</td>
			<td>String</td>
			<td>MAC address of the gateway.</td>
		</tr>
		<tr>
			<td>linkbutton</td>
			<td>Bool</td>
			<td>true if the linkbutton was pressed.</td>
		</tr>
		<tr>
			<td>utc</td>
			<td>String</td>
			<td>Current UTC time of the gateway in ISO 8601 format.</td>
		</tr>
		<tr>
			<td>swversion</td>
			<td>String</td>
			<td>API version as string.</td>
		</tr>
	</tbody>
</table>

#### Possible errors

[403 Not Authorized](/errors#403)

------------------------------------------------------

## Aquire API key<a name="aquireapikey">&nbsp;</a>
Creates a new [API key](/authorization) which provides authorized access to the REST API.

	POST /api

#### Parameters

<table class="table table-bordered">
	<thead>
		<tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
	</thead>
	<tbody>
		<tr>
			<td>devicetype</td>
			<td>String (0..40 chars)</td>
			<td>Name of the client application.</td>
			<td>required</td>
		</tr>
		<tr>
			<td>username</td>
			<td>String (10..40 chars)</td>
			<td>Will be used as username. If not specified a random key will be generated.</td>
			<td>optional</td>
		</tr>
	</tbody>
</table>

### Request

	{
		"username": "988112a4e198cc1211",
		"devicetype": "my application"
	}

### Response

<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "username": "988112a4e198cc1211" } } ]
</code>
</pre>

#### Possible errors

[400 Bad Request](/errors#400)

------------------------------------------------------

## Delete API key<a name="deleteapikey">&nbsp;</a>

Deletes a API key so it could no longer be used.

------------------------------------------------------

## Get full state<a name="getfullstate">&nbsp;</a>

Returns the full state of the gateway including all its lights, groups, scenes and schedules.
