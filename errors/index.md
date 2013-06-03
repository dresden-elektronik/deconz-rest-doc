---
layout: page
title: Error handling
nav: misc
---

## HTTP status codes
Errors might occur for various reasons. Robust applications shall be expect them and not assume that each API call will succeed.

As usual in REST APIs errors are returned as HTTP status codes. The documentation for each API call lists all possible errors wich might occure.

<table class="table">
	<thead><tr><th>Error code</th><th>Name</th><th>Description</th></tr></thead>
	<tbody>
		<tr><td>200</td><td>OK</td><td>Request succeded</td></tr>
		<tr><td>201</td><td>Created</td><td>A new ressource was created</td></tr>
		<tr><td>202</td><td>Accepted</td><td>Request will be processed but isn't finnihsed yet</td></tr>
		<tr><td>400</td><td>Bad request</td><td>The request was not formated as expected or missing parameters</td></tr>
		<tr><td>403</td><td>Forbidden</td><td>The caller has no rights to access the requested URI</td></tr>
		<tr><td>404</td><td>Ressource Not Found</td><td>The requested ressource (light, group, ...) was not found</td></tr>
	</tbody>
</table>

------------------------------------------------------

## JSON error objects

Further details of the errors are available as JSON object in the 	
body.