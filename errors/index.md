---
layout: page
title: Error handling
nav: misc
---

## Errors
Errors might occure for various reasons and robust applications shall be expect them and not assume that each API call will succeed.

As usual in REST APIs errors are returned as HTTP status codes. The documentation for each API call lists all possible errors wich might occure.

Further details of the errors are available as JSON object in the 	
body.

## HTTP status codes

Error code | Description
-----------|------------
200        | OK
201        | Created
202        | Accepted
400        | Bad Request
403        | Not authorized
404        | Ressource not found

## JSON error objects