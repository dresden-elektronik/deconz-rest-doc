---
layout: page
title: About REST
tagline: Documentation
---
{% include JB/setup %}

## Introduction

REST stands for Representational State Transfer and sets the ground for various modern web based APIs.
The main idea behind REST is that everything is a ressource and has a state.

Ressources are represented by a URLs like:

- `/lights` - a collection of lights
- `/lights/1` - a single light
- `/lights/1/state` - the current state of a light

### API Endpoints

All ressources are provided by so called endpoints. The API endpoint documentaion can be found in the menu on the left side.

Currently the following endpoints are available.

<table class="table table-bordered">
	<thead>
		<tr><th>Endpoint</th><th>Description</th></tr>
	</thead>
	<tbody>
		<tr>
			<td><a href="{{BASE_PATH}}/configuration">/config</a></td>
			<td>Interface to query and modify the gateway configuration.</td>
		</tr>
		<tr>
			<td><a href="{{BASE_PATH}}/lights">/lights</a></td>
			<td>Interface for single lights.</td>
		</tr>
		<tr>
			<td><a href="{{BASE_PATH}}/groups">/groups</a></td>
			<td>Interface for groups of lights.</td>
		</tr>
		<tr>
			<td><a href="{{BASE_PATH}}/scenes">/scenes</a></td>
			<td>Interface to the scenes of a group.</td>
		</tr>
		<tr>
			<td><a href="{{BASE_PATH}}/schedules">/schedules</a></td>
			<td>Interface for timed commands.</td>
		</tr>
	</tbody>
</table>

More endpoints and functionality will be added in future.

------------------------------------------------------
## Methods

Ressources can be queried and modified with standard HTTP methods. Where GET, PUT, POST and DELETE are only a subset of all possible methods, they are by far the most used ones.

<table class="table table-bordered">
	<thead><tr><th>Method</th><th>Description</th></tr></thead>
	<tbody>
		<tr><td>GET</td><td>Query the content of a ressource.</td></tr>
		<tr><td>PUT</td><td>Modifies a <strong>existing</strong> ressource.</td></tr>
		<tr><td>POST</td><td>Creates a <strong>new</strong> ressource which did not exist before.</td></tr>
		<tr><td>DELETE</td><td>Deletes a ressource.</td></tr>
	</tbody>
</table>

------------------------------------------------------
## JSON

The contents of ressources are often expressed in Javascript Object Notation better known as JSON. That's not a requirement of REST itself, in fact some APIs also use XML but JSON is by far more popular due its simplicity.

The JSON format is a very simple but powerful notation to express structured objects and lists. The following example covers anything what can be expressed with JSON.

### Example Object

	{
		"a_string": "this is a string",
		"a_number": 5,
		"a_list": [ 1, 2.0, 3, 4 ],
		"a_mixed_list": [ 2, {}, "name", 6, [ 1, 2 ,3 ] ],
		"a_nested_object": {
			 "foo": "bar"
			}
	}

 - Strings are always double quoted `"like this"`
 - keys and values are seperated through a colon `:` and keys are always strings like `"key"`
 - Objects `{ }` and lists `[ ]` might be empty and can be nested
 - Numbers can be integers `1` or fractional `0.5`

Thats all about JSON.

------------------------------------------------------
### URLs and the API key

When reading the API endpoint documentation URLs will look like `/api/<apikey>/lights`.

The first thing to note here is the `/api` prefix which seperates the API interface from the HTML5 web application which is reachable through the document root `/`.

Further nearly any API requests requires a so called **API key** which is a _mandatory_ part of request URLs.

The API key has the single purpose to restrict access to the gateway. Remember the gateway is reachable through the whole local network and without the API key requirement anbody could control the lights.

That said all clients need to [aquire API key]({{BASE_PATH}}/configuration#aquireapikey) through the configuration endpoint.

------------------------------------------------------
### Benefits

 - clients might access the API local or remote via network
 - access from any desktop and mobile platform
 - access from any programming language
 - all popular programming languages provide helper classes and functions to work with RESTful APIs
 - the format of requests and responses is human readable
 - learning and using REST APIs is pretty straight forward

------------------------------------------------------
## What's next
Now you know the basics about REST it's time to move on to the [Getting Started]({{BASE_PATH}}/getting_started) section which explains step by step how to aquire a API key and do some basic control of the lights.
