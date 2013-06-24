---
layout: page
title: Discovery
tagline: Documentation
---
{% include JB/setup %}

## Finding the gateway

The gateway(s) in the local network could be discovered in various ways.

### Discovery via internet

	GET https://dresden-light.appspot.com/discover

This returns a JSON list of all known gateways in the local network.

If both the gateway and the application have access to the internet, discovery via the internet is the easiest way to find the gateway.

#### Response
<pre class="highlight">
<code>
	[{
		"internal_ip": "192.168.192.237",
	 	"internal_port": "80",
	 	"mac": "E0:69:78:58:22:A4:32:CE",
	 	"name": "deCONZ Rpi"
 	}]
</code>
</pre>

`Note` For webapps this is the only way to automatically find the gateway.

By visiting [http://www.dresden-elektronik.de/discover](http://www.dresden-elektronik.de/discover) a list of all gateways in the local network will be displayed.
This is done by only using jQuery, Ajax and internet discovery.

### Discovery via UPnP

Another method to find the gateway is UPnP discovery via UDP sockets.

The main advantage over internet discovery is that no internet is needed at all.

`Note` The discovery might not work as expected if in the local network beside the main router also bridges are used, which might prevent UDP broadcasts to reach the whole network.
