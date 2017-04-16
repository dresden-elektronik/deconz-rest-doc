---
layout: page
title: User parameter
nav: endpoints-hidden
order: 8
anchors:
  - title: Add user parameter
    url: "#add"
  - title: Modify user parameter
    url: "#modify"
  - title: Get all user parameter
    url: "#getall"
  - title: Get user parameter
    url: "#get"
  - title: Delete user parameter
    url: "#delete"
---

{% include JB/setup %}

Provides the ability to store arbitrary data as a key value pair.
Value data is stored treated text and therefore any conversion to other data types must be accomblished in the application.

------------------------------------------------------

## Add user parameter<a name="add">&nbsp;</a>

    POST /api/<apikey>/userparameter/<key>

Creates a new user parameter. The Key is specified in the address. Returns an error if the key already exists. 

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>value</td>
      <td>String</td>
      <td>The value corresponding to the key</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request
<pre class="headers">
<code>
POST /api/12345/userparameter/myparam
</code>
</pre>
<pre class="highlight">
<code>
{
    "This is an example value."
}
</code>
</pre>

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[
    { "success": { "/config/userparameter : added new myparam  }}
]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

------------------------------------------------------

## Modify user parameter<a name="modify">&nbsp;</a>

    PUT /api/<apikey>/userparameter/<key>

Modifies an existing user parameter. The Key is specified in the address. Overwrites the key if it already exists.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>value</td>
      <td>String</td>
      <td>The value corresponding to the key</td>
      <td>required</td>
    </tr>
  </tbody>
</table>

### Example request data
<pre class="headers">
<code>
PUT /api/12345/userparameter/numbers
</code>
</pre>
<pre class="highlight">
<code>
{
    1,2,3,4
}
</code>
</pre>

	
### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[
    { "success": { "/config/userparameter/updated numbers  }}
]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Get all user parameters<a name="getall">&nbsp;</a>

    GET /api/<apikey>/userparameter

Returns a list of all user parameter keys

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
{
  "0": "groupssequenceleft",
  "1": "groupssequenceright"
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
      <td>userparameterkey</td>
      <td>String</td>
      <td>The key of the parameter</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

------------------------------------------------------

## Get user parameter<a name="get">&nbsp;</a>

    GET /api/<apikey>/userparameter/<key>

Returns the key and the corresponding value

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
{
  "groupssequenceleft" : "["3","2","1"]"
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
      <td>key</td>
      <td>String</td>
      <td>The key of the userparameter</td>
    </tr>
    <tr>
      <td>value</td>
      <td>String</td>
      <td>The value corresponding to the key</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)

------------------------------------------------------

## Delete user parameter<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/userparameter/<key>

Removes a user parameter from the gatewaay.

### Parameters

None

### Response
<pre class="headers">
<code>
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "/config/userparameter : key <key> removed  }} ]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[404 Not Found](/errors#404)

------------------------------------------------------