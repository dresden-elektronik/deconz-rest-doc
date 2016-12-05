---
layout: page
title: Userparameter
nav: endpoints
order: 8
anchors:
  - title: Add userparameter
    url: "#add"
  - title: Modify userparameter
    url: "#modify"
  - title: Get all userparameter
    url: "#getall"
  - title: Get userparameter
    url: "#get"
  - title: Delete userparameter
    url: "#delete"
	
---

{% include JB/setup %}

Provides the opportunity to save your own parameter as a key vaule pair.
The value is simple text and don't need to be in json format.

------------------------------------------------------

## Add userparameter<a name="add">&nbsp;</a>

    POST /api/<apikey>/userparameter/<key>

Modifies an existing userparameter. The Key is specified in the address. Returns an error if the key already exists. 

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
    </tr>
  </tbody>
</table>

### Example request data
    {
	    "This is an example value."
    }

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
    { "success": { "/config/userparameter : updated <key>  }}
]
</code>
</pre>

### Possible errors

[400 Bad Request](/errors#400)

[403 Forbidden](/errors#403)

[404 Not Found](/errors#404)


------------------------------------------------------

## Modify userparameter<a name="modify">&nbsp;</a>

    PUT /api/<apikey>/userparameter/<key>

Modifies an existing userparameter. The Key is specified in the address. Overwrites the key if it already exists.

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
    </tr>
  </tbody>
</table>

### Example request data
    {
	    1,2,3,4
    }
	
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

## Get all userparameter<a name="getall">&nbsp;</a>

    GET /api/<apikey>/userparameter

Returns a list of all userparameter keys

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

## Get userparameter<a name="get">&nbsp;</a>

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

## Delete userparameter<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/userparameter/<key>

Removes a userparameter from the gatewaay.

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