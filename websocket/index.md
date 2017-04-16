---
layout: page
title: Websocket
nav: endpoints
order: 10
anchors:
  - title: Query server port
    url: "#port"
  - title: Open connection
    url: "#connect"
  - title: Message format
    url: "#format"
---

{% include JB/setup %}

The embedded Websocket server provides push notifications for applications which require real-time feedback from devices like light switches and motion sensors.

`since` version 2.04.40

## Query server port<a name="port">&nbsp;</a>


The Websocket server is started on an unused proxy friendly port which, depending on the system, is either 443, 8088, 8088, 20877 or any other unused random port.

The used port is listed in the configuration.

    GET /api/<apikey>/config


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
    "websocketport": 8088,
    ...
}
</code>
</pre>

### Possible errors

[403 Forbidden](/errors#403)

[503 Service Unavailable](/errors#503)

------------------------------------------------------

## Open connection<a name="connection">&nbsp;</a>

How to establish a connection to an websocket server depends on the underlying programming environment.

### Javascript example
The following example demonstrates how to establish a connection with Javascript in a browser or NodeJS implementation.

    var host = '192.168.1.202';
    var port = 8088;

    var ws = new WebSocket('ws://' + host + ':' + port);

    ws.onmessage = function(msg) {
        console.log( JSON.parse(msg.data) );
    }

------------------------------------------------------

## Message format<a name="format">&nbsp;</a>

Messages received over a Websocket connection contain data in JSON format.

##### Sensor button event example

    {
        "t": "event",
        "e": "changed",
        "r": "sensors",
        "id": "12",
        "state": { "buttonevent": 2002 }
    }

##### Sensor presence signal example

    {
        "t": "event",
        "e": "changed",
        "r": "sensors",
        "id": "7",
        "state": { "presence": true }
    }

#### Message fields

<table class="table table-bordered">
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>t</td>
            <td>String</td>
            <td>
                Specifies the message type:
                <ul>
                    <li>event - the message hold an event</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>e</td>
            <td>String</td>
            <td>
                Specifies the type of an <em>event</em> message:
                <ul>
                    <li>changed - resource attributes have changed</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>r</td>
            <td>String</td>
            <td>
                Type of resource to which the message belongs:
                <ul>
                    <li>sensors - the id field refers to a sensor resource</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>id</td>
            <td>String</td>
            <td>The id of a resource like /sensors/8</td>
        </tr>
    </tbody>
</table>
