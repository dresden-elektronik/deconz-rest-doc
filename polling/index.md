---
layout: page
title: Polling
nav: misc
---

## Polling state

Since the state of lights and groups might be changed from various devices, client applications shall update their local cache regularly to provide the best user expierience.

To keep the processing overhead low in the gateway as well as on the client the API supports the common HTTP `ETag` and `If-None-Match` headers to prevent full state updates in each polling attemp.

## ETag HTTP header

Many API calls return a ETag in the HTTP header. A ETag is a hash string which belongs to a ressource and is changed every time the ressource is modfied.

Ressources are:
 - lights
 - groups
 - configuration

For example the first API call to get the state of light 1 returns a ETag.
In a second call the client provides the HTTP header field `If-None-Match` with the latest known ETag of the light.

 - If the light meanwhile has changed the request will return the new state and another ETag.

 - If the light wasn't changed a HTTP status `304 Not Modified` will be returned with no body content, in this case the client don't need to update any data or UI. 

