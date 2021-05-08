---
title: Rules
---

# Rules

Rules provide the ability to trigger actions of lights or groups when a specific sensor condition is met.

## Create rule<a name="create">&nbsp;</a>

    POST /api/<apikey>/rules

Creates a new rule.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>actions</td>
      <td>Array (1&ndash;8)</td>
      <td>An array of actions that will happen when the rule triggers.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>action.address</td>
      <td>String</td>
      <td>path to a light, group or scene resource</td>
      <td>required</td>
    </tr>
    <tr>
      <td>action.body</td>
      <td>Object</td>
      <td>Parameters that will be send to the resource formated as JSON.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>action.method</td>
      <td>String</td>
      <td>Can be PUT, POST or DELETE.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>conditions</td>
      <td>Array(condition) (1&ndash;8)</td>
      <td>The conditions that must be met to trigger a rule.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>condition.address</td>
      <td>String</td>
      <td>path to a sensor resource and the related state</td>
      <td>required</td>
    </tr>
    <tr>
      <td>condition.operator</td>
      <td>String</td>
      <td><b>eq</b>, <b>gt</b>, <b>lt</b>, <b>dx</b> (equals, greater than, lower than, on change).</td>
      <td>required</td>
    </tr>
    <tr>
      <td>condition.value</td>
      <td>String</td>
      <td>The value the operator is compared with. Will be casted automatically to the corresponding data type.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the rule.</td>
      <td>required</td>
    </tr>
    <tr>
      <td>periodic</td>
      <td>Number</td>
      <td>Specifies if the rule should trigger periodically. 0 = trigger on event; >0 = time in ms the rule will be triggered periodically. Default is 0.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>status</td>
      <td>String</td>
      <td>The status of the rule, either "enabled" or "disabled". Default is "enabled".</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data

<pre class="highlight">
<code>
{
    "actions": [
        {
            "address": "/groups/0/action",
            "body": {
                "on": true
            },
            "method": "BIND"
        }
    ],
    "conditions": [
        {
            "address": "/sensors/1/state/buttonevent",
            "operator": "eq",
            "value": "1"
        }
    ],
    "name": "Switch button 1 all lights On/Off"
}
</code>
</pre>

This will create a binding between a switch and the On/Off Cluster of all Lights of the group 0.

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "1" } } ]
</code>
</pre>

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>String</td>
      <td>The unique identifier of the new rule.</td>
    </tr>
  </tbody>
</table>


### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get all Rules<a name="getall">&nbsp;</a>

    GET /api/<apikey>/rules

Returns a list of all rules. If there are no rules in the system then an empty object {} will be returned.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
{
    "1": {
        "actions": [
            {
                "address": "/lights/1/state",
                "body": {
                    "on": true
                },
                "method": "BIND"
            }
        ],
        "conditions": [
            {
                "address": "/sensors/2/state/buttonevent",
                "operator": "eq",
                "value": "4"
            }
        ],
        "created": "2016-07-04T14:17:12",
        "etag": "9bd1fcc627001458ea88c8742e61c692",
        "lasttriggered": "none",
        "name": "Sensor: 2 EP:4 On/Off",
        "owner": "AD4F14F244",
        "periodic": 0,
        "status": "enabled",
        "timestriggered": 0
    },
    "2": {
        "actions": [
            {
                "address": "/groups/0/action",
                "body": {
                    "on": false
                },
                "method": "PUT"
            }
        ],
        "conditions": [
            {
                "address": "/sensors/5/state/buttonevent",
                "operator": "eq",
                "value": "34"
            },
            {
                "address": "/sensors/5/state/lastupdated",
                "operator": "dx"
            }
        ],
        "created": "2016-07-05T13:36:52",
        "etag": "0fb118418fa77116052f74fb129a648b",
        "lasttriggered": "none",
        "name": "0x0000000000402483[Rule1]",
        "owner": "AD4F14F244",
        "periodic": 0,
        "status": "enabled",
        "timestriggered": 0
    }
}
</code>
</pre>

#### Response fields

The whole rule object as descripted in [Get rule](#getrule).

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get rule<a name="getrule">&nbsp;</a>

    GET /api/<apikey>/rules/<id>

Returns the rule with the specified id.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
{
    "actions": [
        {
            "address": "/lights/1/state",
            "body": {
                "on": true
            },
            "method": "BIND"
        }
    ],
    "conditions": [
        {
            "address": "/sensors/2/state/buttonevent",
            "operator": "eq",
            "value": "4"
        }
    ],
    "created": "2016-07-04T14:17:12",
    "etag": "9bd1fcc627001458ea88c8742e61c692",
    "lasttriggered": "none",
    "name": "Sensor: 2 EP:4 On/Off",
    "owner": "AD4F14F244",
    "periodic": 0,
    "status": "enabled",
    "timestriggered": 0
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
      <td>actions</td>
      <td>Array</td>
      <td>An array of actions that will happen when the rule triggers.</td>
    </tr>
    <tr>
      <td>action.address</td>
      <td>String</td>
      <td>path to a light, group or scene resource</td>
    </tr>
    <tr>
      <td>action.body</td>
      <td>Object</td>
      <td>Parameters that will be send to the resource formated as JSON.</td>
    </tr>
    <tr>
      <td>action.method</td>
      <td>String</td>
      <td>Can be PUT, POST or DELETE.</td>
    </tr>
    <tr>
      <td>conditions</td>
      <td>Array</td>
      <td>The conditions that must be met to trigger a rule.</td>
    </tr>
    <tr>
      <td>condition.address</td>
      <td>String</td>
      <td>path to a sensor resource</td>
    </tr>
    <tr>
      <td>condition.operator</td>
      <td>String</td>
      <td>eq, gt, lt, dx (equals, greater than, lower than, on change).</td>
    </tr>
    <tr>
      <td>condition.value</td>
      <td>String</td>
      <td>The value the operator is compared with. Will be casted automatically to the corresponding data type.</td>
    </tr>
    <tr>
      <td>created</td>
      <td>String</td>
      <td>Timestamp when the rule was created.</td>
    </tr>
    <tr>
      <td>etag</td>
      <td>String</td>
      <td>HTTP <a href="../../misc/polling#etag">etag</a> which changes whenever the rule is changed.</td>
    </tr>
    <tr>
      <td>lasttriggered</td>
      <td>String</td>
      <td>Timestamp when the rule was last triggered.</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the rule.</td>
    </tr>
    <tr>
      <td>owner</td>
      <td>String</td>
      <td>The owner of the rule.</td>
    </tr>
    <tr>
      <td>periodic</td>
      <td>Number</td>
      <td>Specifies if the rule should trigger periodically. 0 = trigger on event; >0 = time in ms the rule will be triggered periodically.</td>
    </tr>
    <tr>
      <td>status</td>
      <td>String</td>
      <td>The status of the rule, either "enabled" or "disabled".</td>
    </tr>
    <tr>
      <td>timestriggered</td>
      <td>Number</td>
      <td>Times the rule was triggered.</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Update rule<a name="update">&nbsp;</a>

    PUT /api/<apikey>/rules/<id>/

Update a rule with the specified parameters.

### Parameters

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th>Required</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>actions</td>
      <td>Array (1&ndash;8)</td>
      <td>An array of actions that will happen when the rule triggers.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>conditions</td>
      <td>Array (1&ndash;8)</td>
      <td>The conditions that must be met to trigger a rule.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>The name of the rule.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>periodic</td>
      <td>Number</td>
      <td>Specifies if the rule should trigger periodically. 0 = trigger on event; >0 = time in ms the rule will be triggered periodically. Default is 0.</td>
      <td>optional</td>
    </tr>
    <tr>
      <td>status</td>
      <td>String</td>
      <td>The status of the rule, either "enabled" or "disabled", the default is "enabled".</td>
      <td>optional</td>
    </tr>
  </tbody>
</table>

### Example request data

    {
      "actions": [
            {
                "address": "/lights/1/state",
                "body": {
                    "bri": 1
                },
                "method": "BIND"
            }
        ]
    }

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[
    {
        "success": { "/rules/1/actions":
            {
                "address": "/lights/1/state",
                "body": {
                    "bri": 1
                },
                "method": "BIND"
            }
        }
    }
]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Delete rule<a name="delete">&nbsp;</a>

    DELETE /api/<apikey>/rules/<id>

Delete a rule.

### Parameters

None

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
ETag: "030cf8c1c0025420f3a0659afab251f5"
</code>
</pre>
<pre class="highlight">
<code>
[{ "success": "1"}]
</code>
</pre>

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)
