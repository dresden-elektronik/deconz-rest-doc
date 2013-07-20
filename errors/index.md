---
layout: page
title: Error handling
nav: misc
---
{% include JB/setup %}

## HTTP status codes
Errors might occur for various reasons. Robust applications shall handle them and not assume that each API call will succeed.

As usual in REST APIs errors are returned as HTTP status codes. The documentation for each API call lists all possible errors which might occur.

<table class="table">
	<thead><tr><th>Error code</th><th>Name</th><th>Description</th></tr></thead>
	<tbody>
		<tr><td>200</td><td>OK</td><td>Request succeded</td></tr>
		<tr><td>201</td><td>Created</td><td>A new resource was created</td></tr>
		<tr><td>202</td><td>Accepted</td><td>Request will be processed but isn't finished yet</td></tr>
		<tr><td>304</td><td>Not Modified</td><td>Is returned if the request had the If-None-Match header and the ETag on the resource was the same.</td></tr>
		<tr><td>400</td><td>Bad request</td><td>The request was not formated as expected or missing parameters</td></tr>
		<tr><td>403</td><td>Forbidden</td><td>The caller has no rights to access the requested URI</td></tr>
		<tr><td>404</td><td>Resource Not Found</td><td>The requested resource (light, group, ...) was not found</td></tr>
		<tr><td>503</td><td>Service Unavailable</td><td>The device is not connected to the network or too busy to handle further requests</td></tr>
	</tbody>
</table>

------------------------------------------------------

## JSON error objects

Further details of the errors are available as JSON object in the 	
response body.

	{
		"error": {
			"type": <error code>,
			"address": <ressource/parameter>,
			"description": <description>
		}
	}

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>type</td>
      <td>Number</td>
      <td>One of the error codes listed below.</td>
    </tr>
    <tr>
      <td>address</td>
      <td>String</td>
      <td>The url which refers to the resource/parameter which caused the error.</td>
    </tr>
    <tr>
      <td>description</td>
      <td>String</td>
      <td>The error description contains details on what went wrong.</td>
    </tr>
  </tbody>
</table>

### Errors

<table class="table table-bordered">
  <thead>
    <tr><th>Error</th><th>Description</th><th>Details</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>unauthorized user</td>
      <td>This will be returned if the request had no valid <b>apikey</b> or if the apikey has not the rights to access a resource.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>body contains invalid JSON</td>
      <td>This will be returned if the JSON in the body couldn't be parsed.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>resource, <code>&lt;resource&gt;</code>, not available</td>
      <td>This will be returned if the requestet resource like a light or a group does not exist.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>method, <code>&lt;method&gt;</code>, not available for resource, <code>&lt;resource&gt;</code></td>
      <td>This will be returned if the requested method (GET, PUT, POST or DELETE) is not supported for the resource.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>missing parameters in body</td>
      <td>This will be returned if the request didn't contain all required parameters.</td>
    </tr>
    <tr>
      <td>6</td>
      <td>parameter, <code>&lt;parameter&gt;</code>, not available</td>
      <td>This will be returned if a parameter sent in the request is not supported.</td>
    </tr>
    <tr>
      <td>7</td>
      <td>invalid value, <code>&lt;value&gt;</code>, for parameter, <code>&lt;parameter&gt;</code></td>
      <td>This will be returned if a parameter hasn't the expected format or is out of range.</td>
    </tr>
    <tr>
      <td>8</td>
      <td>parameter, <code>&lt;parameter&gt;</code>, is not modifiable</td>
      <td>This will be returned in an attempt to change a read only parameter.</td>
    </tr>
  </tbody>
</table>