---
title: Touchlink
---

# Touchlink

The touchlink endpoint allows to communicate with near by located devices.

## Scan for devices<a name="scan">&nbsp;</a>

    POST /api/<apikey>/touchlink/scan

Starts scanning on all channels for devices which are located close to the gateway. The whole scan process will take about 10 seconds.

!!! note
    While scanning is in progress further API requests which require network access aren't allowed.

### Parameters

None

### Response

<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Get scan results<a name="getscanresults">&nbsp;</a>

    GET /api/<apikey>/touchlink/scan

Returns the results of a touchlink scan.

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
    "scanstate": "scanning",
    "lastscan": "2013-11-05T08:14:12",
    "result": {
        "1": {
            "factorynew": true,
            "address": "0x0017880100bfbfed"
        },
        "2": {
            "factorynew": false,
            "address": "0x001788010022b40a"
        }
     },
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
            <td>scanstate</td>
            <td>String</td>
            <td>
                State of a scan request:
                <ul>
                    <li>idle - scan is finished or was not started</li>
                    <li>scanning - scan is in progress</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>lastscan</td>
            <td>String</td>
            <td>UTC time of the last scan in ISO 8601 format.</td>
        </tr>
        <tr>
            <td>result</td>
            <td>Object</td>
            <td>A list of all devices which where found during the scan.</td>
        </tr>
    </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Identify a device<a name="identify">&nbsp;</a>

    POST /api/<apikey>/touchlink/<id>/identify

Puts a device into identify mode for example a light will blink a few times.

!!! note
    <i>id</i> must be one of the indentifiers which are returned in the scan result.

### Parameters

None

### Response

<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)

------------------------------------------------------

## Reset a device<a name="reset">&nbsp;</a>

    POST /api/<apikey>/touchlink/<id>/reset

Send a reset to factory new request to a device.

!!! note
    <i>id</i> must be one of the indentifiers which are returned in the scan result.

### Parameters

None

### Response

<pre class="headers">
<code>
HTTP/1.1 200 OK
</code>
</pre>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

[503 Service Unavailable](../../misc/errors#503)
