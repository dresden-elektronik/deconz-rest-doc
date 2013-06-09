---
layout: page
title: Authorization
nav: misc
---

## API Keys
Apps which want to access the API must optain a API key. There are two methods for doing so.

- Unlocking the gateway
- HTTP basic authentification

## Unlocking the gateway
Unlocking the gateway for a short period of time allows any app to [acquire a API key](/configuration#aquireapikey) via configuration API.

To unlock the gateway for 30 seconds visit the gateway main page ([see discovery](/discovery)) in the browser and choose `Settings/Account` from the top menu. On the accounts page click on the `unlock 30 seconds` button in order to unlock the gateway.

In the next 30 seconds any app may aquire a new API key.

## HTTP basic authentification
Apps might want to retreive a API key without the need that the user must unlock the gatway.
This could be achieved by asking the user for the gateway username and password and handover the credentials
in the [Acquire API key](/configuration#aquireapikey) call via HTTP basic authentification.

The API call needs to be extended with HTTP header field `Authorization` as follows:

	Authorization: Basic <credential-hash>

there &lt;credential-hash&gt; is the base64 encoded version of `username:password`.
