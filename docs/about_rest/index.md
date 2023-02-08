---
title: About REST

---

# About REST

REST stands for Representational State Transfer and sets the ground for various modern web based APIs.
The main idea behind REST is that everything is a resource and has a state.

Resources are represented by URLs like:

- `/lights` - a collection of lights
- `/lights/1` - a single light
- `/lights/1/state` - the current state of a light

## API endpoints

All resources are provided by so called endpoints. The API endpoint documentation can be found in the menu on the left side.

Currently the following endpoints are available.


Endpoint                              | Description
--------------------------------------|--------------------------
[/alarmsystems](../endpoints/configuration) | Query and modify alarm systems configuration.
[/config](../endpoints/configuration) | Query and modify the gateway configuration.
[/lights](../endpoints/lights)        | Query and control lights.
[/sensors](../endpoints/sensors)      | Query and control sensors.
[/groups](../endpoints/groups)        | Setup groups and scenes with lights and control them.
[/ruless](../endpoints/groups)        | Manage the ability to trigger actions of lights or groups.
[/scenes](../endpoints/scenes)        | Setup and control scenes of a group.
[/schedules](../endpoints/schedules)  | Created time based schedules.
[/touchlink](../endpoints/touchlink)  | Execute Zigbee Light Link touchlink commands.


------------------------------------------------------

## Methods

Resources can be queried and modified with standard HTTP methods. Where GET, PUT, POST and DELETE are only a subset of all possible methods, they are by far the most used ones.

<table class="table table-bordered">
	<thead><tr><th>Method</th><th>Description</th></tr></thead>
	<tbody>
		<tr><td>GET</td><td>Query the content of a resource.</td></tr>
		<tr><td>PUT</td><td>Modifies a <strong>existing</strong> resource.</td></tr>
		<tr><td>POST</td><td>Creates a <strong>new</strong> resource which did not exist before.</td></tr>
		<tr><td>DELETE</td><td>Deletes a resource.</td></tr>
	</tbody>
</table>

------------------------------------------------------

## JSON

The contents of resources are often expressed in Javascript Object Notation better known as JSON. That's not a requirement of REST itself, in fact some APIs also use XML but JSON is by far more popular due to its simplicity.

The JSON format is a very simple but powerful notation to express structured objects and lists. The following example covers everything that can be expressed with JSON.

**Example object**

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
 - Keys and values are separated by a colon `:` and keys are always strings like `"key"`
 - Objects `{ }` and lists `[ ]` might be empty and can be nested
 - Numbers can be integers `1` or fractional `0.5`

That's all about JSON.

------------------------------------------------------

## URLs and the API key

When reading the API endpoint documentation URLs will look like `/api/<apikey>/lights`.

The `/api` prefix separates the API interface from the HTML5 web application which is reachable through the document root `/`.

Nearly every API request requires a so called **API key** which is a _mandatory_ part of request URLs.

The API key has the only purpose to restrict access to the gateway. Remember the gateway is reachable through the whole local network and without the API key requirement anybody could control the lights.

Nevertheless all clients need to [acquire API key](../endpoints/configuration#aquireapikey) by means of the configuration endpoint.

------------------------------------------------------

## Benefits

 - Clients might access the API local or remote via network
 - Access from any desktop and mobile platform
 - Access from any programming language
 - All popular programming languages provide helper classes and functions to work with RESTful APIs
 - The format of requests and responses is human readable
 - Learning and using REST APIs is pretty straight forward

------------------------------------------------------

## What's next
Now you know the basics about REST. It's time to move on to the [Getting Started](../getting_started) section which explains step by step how to acquire an API key and do some basic control of the lights.
