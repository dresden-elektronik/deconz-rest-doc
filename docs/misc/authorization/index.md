---
title: Authorization
---

# Authorization

--------

## API keys

Apps which want to access the API must obtain an API key. There are two methods for doing so.

- Unlocking the gateway
- HTTP basic authentification

## Unlocking the gateway

Unlocking the gateway for a short period of time allows any app to [acquire an API key](../../endpoints/configuration#aquireapikey) via configuration API.

To unlock the gateway for 60 seconds visit the gateway main page in the browser and choose `Settings/System` from the top menu. On the system page click on the `unlock` button in order to unlock the gateway, see [Discovery](../discovery).

In the next 60 seconds any app may acquire a new API key.

## HTTP basic authentication

Apps might want to receive an API key without the need that the user must unlock the gateway.
This could be achieved by asking the user for the gateway username and password and handover the credentials
in the [Acquire API key](../../endpoints/configuration#aquireapikey) call via HTTP basic authentification.

The API call needs to be extended with HTTP header field `Authorization` as follows:

	Authorization: Basic <credential-hash>

There &lt;credential-hash&gt; is the base64 encoded version of `username:password`.
