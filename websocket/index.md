---
layout: page
title: Websocket
nav: endpoints
order: 10
anchors:
  - title: Websocket Configuration
    url: "#port"
  - title: Open Connection
    url: "#connect"
  - title: Message Format
    url: "#format"
---

{% include JB/setup %}

The embedded Websocket server provides push notifications to applications which require real-time feedback from devices like lights, groups, switches, and sensors.

`since` version 2.04.40

## Websocket Configuration<a name="port">&nbsp;</a>


The Websocket server is started on an unused proxy friendly port which, depending on the system, is either 443, 8080, 8088, 20877, or any other unused random port.

The Websocket server can be configured to include all `state` or `config` attributes in the message, or only the changed attributes.

The Websocket used port and setting are listed in the configuration API endpoint:

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
    ...
    "websocketnotifyall": true,
    "websocketport": 8088,
    ...
}
</code>
</pre>

### Possible errors

[403 Forbidden](/errors#403)

[503 Service Unavailable](/errors#503)

------------------------------------------------------

## Open Connection<a name="connection">&nbsp;</a>

How to establish a connection to a Websocket server depends on the underlying programming environment.

### Javascript example
The following example demonstrates how to establish a connection with Javascript in a browser or NodeJS implementation.
```javascript
const WebSocket = require('ws');

const host = '192.168.1.202';
const port = 8088;

const ws = new WebSocket('ws://' + host + ':' + port);

ws.onmessage = function(msg) {
    console.log(JSON.parse(msg.data));
}
```
------------------------------------------------------

## Message Format<a name="format">&nbsp;</a>

Messages received over a Websocket connection contain data in JSON format.

##### Light state change example
```json
{
    "e": "changed",
    "id": "1",
    "r": "lights",
    "state": {
        "bri": 1,
        "on": true,
        "x": 65279,
        "xy": [
            0.9961,
            0.9961
        ],
        "y": 65279
    },
    "t": "event",
    "uniqueid": "00:0b:57:ff:fe:9a:46:ab-01"
}
```
Note that `x` and `y` are included in the `state` for backwards compatibility.
New apps should use `xy` instead.

##### Group state change example
```json
{
    "e": "changed",
    "id": "1",
    "r": "groups",
    "state": {
        "all_on": true,
        "any_on": true
    },
    "t": "event"
}

```

##### Sensor button event example
```json
{
    "e": "changed",
    "id": "5",
    "r": "sensors",
    "state": {
        "buttonevent": 2002,
        "lastupdated": "2019-03-15T20:16:30"
    },
    "t": "event",
    "uniqueid": "00:0d:6f:00:10:65:8a:6e-01-1000"
}
```

#### Message fields

<table class="table table-bordered">
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
    <tr>
            <td>`t`</td>
            <td>String</td>
            <td>
                The **type** of the message:
                <ul>
                    <li>`event` - the message holds an event.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>`r`</td>
            <td>String</td>
            <td>
                The **resource type** to which the message belongs:
                <ul>
                    <li>`groups` - the `id` field refers to a group resource;</li>
                    <li>`lights` - the `id` field refers to a light resource;</li>
                    <li>`sensors` - the `id` field refers to a sensor resource.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>`e`</td>
            <td>String</td>
            <td>
                The **event type** of the message:
                <ul>
                    <li>`added` - resource has been added;</li>
                    <li>`changed` - resource attributes have changed;</li>
                    <li>`deleted` - resource has been deleted.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>`id`</td>
            <td>String</td>
            <td>The id of the resource to which the message belongs, e.g. `5` for `/sensors/5`.</td>
        </tr>
        <tr>
            <td>`uniqueid`</td>
            <td>String</td>
            <td>The `uniqueid` of the resource to which the message belongs, e.g. `00:0d:6f:00:10:65:8a:6e-01-1000`.<br>
            Only for light and sensor resources.</td>
        </tr>
        <tr>
            <td>`config`</td>
            <td>Map</td>
            <td>
                Depending on the `websocketnotifyall` setting: a map containing all or only the changed `config` attributes of a sensor resource.<br>
                Only for `changed` events.
            </td>
        </tr>
        <tr>
            <td>`name`</td>
            <td>String</td>
            <td>The (new) name of a resource.<br>
            Only for `changed` events.</td>
        </tr>
        <tr>
            <td>`state`</td>
            <td>Map</td>
            <td>
                Depending on the `websocketnotifyall` setting: a map containing all or only the changed `state` attributes of a group, light, or sensor resource.<br>
                Only for `changed` events.
            </td>
        </tr>
    </tbody>
</table>

Note that only one of `config`, `name`, or `state` will be present per `changed` event.
