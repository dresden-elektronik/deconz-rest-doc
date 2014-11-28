---
layout: page
title: Discovery
tagline: Documentation
---
{% include JB/setup %}

## Finding the gateway

The gateway(s) in the local network can be discovered in various ways.

------------------------------------------------------

### Discovery via internet

	GET https://dresden-light.appspot.com/discover

This returns a JSON list of all known gateways in the local network.

If both the gateway and the application have access to the internet, discovery via the internet is the easiest way to find the gateway.

#### Response
<pre class="highlight">
<code>
	[{
		"id": "E0:69:78:58:22:A4:32:CE",
		"internalipaddress": "192.168.192.34",
	 	"internalport": "8080",
	 	"macaddress": "E0:69:78:58:22:A4:32:CE",
	 	"name": "RaspBee GW"
 	}]
</code>
</pre>

`Note` For webapps this is the only way to automatically find the gateway.

By visiting [http://www.dresden-elektronik.de/discover](http://www.dresden-elektronik.de/discover) a list of all gateways in the local network will be displayed.
This is done by only using jQuery, Ajax and internet discovery.

------------------------------------------------------

### Discovery via UPnP

Another method to find the gateway is UPnP discovery via UDP sockets.

The main advantage compared to the internet discovery is that no internet is needed at all.

`Note` The discovery might not work as expected if in the local network beside the main router also bridges are used, which might prevent UDP broadcasts to reach the whole network.

------------------------------------------------------

### Discovery via nmap

[Nmap](http://www.nmap.org) is an open source command-line network scanner which is available for all major platforms. Since the gateway runs a SSH deamon at port 22 it is easy to find it in the local network.

	$ nmap -p 22 -T5 -n -min-parallelism 100 --open 192.168.192.0/24

`Note` Replace the `192.168.192.0/24` with your subnetwork for example `192.168.0.0/24`.

#### Result

	Starting Nmap 6.25 ( http://nmap.org ) at 2013-07-01 13:04 CEST
	Nmap scan report for 192.168.192.34
	Host is up (0.00081s latency).
	PORT   STATE SERVICE
	22/tcp open  ssh


