---
title: Device Description Files (DDF)
---

# Device Description Files (DDF)

<mark>Work in progress</mark>

!!! Important
    This page serves as a Request For Comments (RFC). This API is not yet available in a release.


The **/ddf** endpoint provides query and management calls for DDF bundles.

### DDF bundles

A DDF bundle is a single self contained **immutable** file which embeds the DDF JSON and all dependencies like scripts and other files, see: [specification](https://github.com/deconz-community/ddf-tools/blob/main/packages/bundler/README.md).

#### Problems with plain DDF JSON files

While DDF system improved the C++ mess, it still has the same issues which can also be found in ZHA and Zigbee2Mqtt device integrations:

- Global updates bound to a deCONZ release.
  When a new release comes out, it's all or nothing every device gets the newest DDF JSON but also its dependencies like scripts, which may be used and changed for other devices, introducing unforseen bugs.
- When something breaks, **and this happens**, perhaps since a script or DDF JSON was updated, there is no way back, other than downgrading of deCONZ.
- Distributing new DDF files is cumbersome, and when external scripts are referenced even more so.
- Users have to wait for new deCONZ releases for latest official DDFs updates.


#### What DDF bundles solve

- Easy exchange during development, just send the DDF bundle to a user.
- Decoupling from deCONZ releases.
- Support for multiple versions for a bundle, e.g. run a new beta version only on one test device.
- Support switching between bundle versions for a device, e.g. if v1.0.1 doesn't work user can switch back to v1.0.0.
- Bundles are immutable and signed, this drastically reduces the chance of breaking a device integration.
- A bundle can't break another one, even if it's using the same external dependencies.

From a users perspective there won't be all or nothing updates dependend on a deCONZ version. Instead DDF updates are explicit like this simplified UI:

> DDF update available for *"Kitchen motion sensor"* (model id: SML003).</br>
> Currently installed version: **v1.2.1** </br>
> Update to version **v1.2.5**? (yes/no/all)


## DDF bundle pinning

!!! Todo
    Currently this page only describes how to query bundle information and upload bundles.
    To actually assign/pin DDF bundles to a device `uniqueid`, the `/devices`
    endpoint needs to be extended.

The following tasks need to be clarified:

- **Initial behaviour** when a device is joined it should automatically be assigned to a suiteable bundle, with the newest version, ideally a bundle that is signed with a "stable" signature.
- **Manual update** Once a device is pinned to a bundle, updating to a new DDF bundle version needs to be done explicitly.
  Like `PUT /api/<apikey>/devices/<uniqueid>/usebundle/<sha256>`, where the bundle with SHA-256 hash itself was [Uploaded](#uploadddfbundle) before.
- **Auto updates** could be made an option, like auto update stable signed bundles. Each deCONZ release does contain the latest official DDF bundles. In future these can also be updated by loading fresh ones from the DDF store which doesn't depend on a deCONZ release.

------------------------------------------------------

## Get all DDF bundle descriptors<a name="getallddfbundledescriptors">&nbsp;</a>

    GET /api/<apikey>/ddf/descriptors

Returns the descriptors of all available DDF bundles.

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

  "12f39fa2bc4db1990715318e749d6270139609c68fb651a70c59339a91207450": {
    "version": "1.2.5",
    "version_deconz": ">2.19.3",
    "last_modified": "2023-04-13T11:54:25Z",
    "product": "STARKVIND Air purifier",
    "device_identifiers": [
      [
        "IKEA of Sweden",
        "STARKVIND Air purifier"
      ],
      [
        "IKEA of Sweden",
        "STARKVIND Air purifier table"
      ]
    ]
  }
}
</code>
</pre>

!!! TODO
    It might be useful to also return the bundle signatures, so a UI can show: offical, stable, beta and user labels.

#### Response fields

The keys in the returned object are the SHA-256 hashes of the immutable data in the DDF bundles (hash over DDFB section).

See <a href="#getddfbundledescriptor">Get DDF bundle descriptor</a> for a full description of the attributes.


### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get DDF bundle descriptor<a name="getddfbundledescriptor">&nbsp;</a>

    GET /api/<apikey>/ddf/descriptors/<sha256-hash>

Returns the descriptor of a DDF bundle.

!!! Note
    This request is useful to retreive the active DDF bundle descriptor of a
    device which can be retreived with the ``/devices/<uniqueid>` endpoint (wip).
    The idea here is to **pin** a bundle via it's sha256-hash to a device identified by its
    MAC address.


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
    "version": "1.2.5",
    "version_deconz": ">2.19.3",
    "last_modified": "2023-04-13T11:54:25Z",
    "product": "STARKVIND Air purifier",
    "device_identifiers": [
      [
        "IKEA of Sweden",
        "STARKVIND Air purifier"
      ],
      [
        "IKEA of Sweden",
        "STARKVIND Air purifier table"
      ]
    ]
}
</code>
</pre>

!!! TODO
    It might be useful to also return the bundle signatures, so a UI can show: offical, stable, beta and user labels.
    Since the signatures are made over the SHA-256 hash it's easy to verify them without loading the full bundle.

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>version</td>
      <td>String</td>
      <td>The semantic version of a bundle.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>version_deconz</td>
      <td>String</td>
      <td>deCONZ versions requirements to run the bundle.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>last_modified</td>
      <td>ISO 8601 timestamp</td>
      <td>Timestamp when the bundle was last modified.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>product</td>
      <td>String</td>
      <td>Human readable product name.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>device_identifiers</td>
      <td>Array</td>
      <td>Pairs of Zigbee manufacturer name and model id</br>from the Basic cluster.</td>
      <td>R</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Upload DDF bundle<a name="uploadddfbundle">&nbsp;</a>

    POST /api/<apikey>/ddf/bundles

Uploads a DDF bundle so it can be used by DDF system.

### Parameters

The DDF bundle is uploaded as `multipart/form-data`, which is used by HTML form input elements with `type="file"` (see: [MSDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition)).

### Example request data

```raw
POST /api/12345/ddf/bundles HTTP/1.1

Content-Type: multipart/form-data;boundary="abcdef"

--abcdef
Content-Disposition: form-data; name="ddfbundle"; filename="example.ddf"

    ....... DDF bundle data .....
--abcdef--
```

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
[ { "success": { "id": "12f39fa2bc4db1990715318e749d6270139609c68fb651a70c59339a91207450" } } ]
</code>
</pre>

The returned **id** is the DDF bundle SHA-256 hash.

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------
