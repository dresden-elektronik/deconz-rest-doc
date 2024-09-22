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

!!! Todo
    Currently this page only describes how to query bundle information and upload bundles.
    To actually assign/pin DDF bundles to a device `uniqueid`, the `/devices`
    endpoint needs to be extended.

## DDF bundle pinning

- **Initial behaviour** when a device is joined it is automatically be assigned to a suitable bundle, with priority on the newest bundle that is signed with a "stable" signature and if not found the latest "beta" or unsigned bundle.
- **Manual update** Once a device is pinned to a bundle, updating to a new DDF bundle version needs to be done explicitly.
  Like `PUT /api/<apikey>/devices/<uniqueid>/usebundle/<sha256>`, where the bundle with SHA-256 hash itself was [Uploaded](#uploadddfbundle) before.
- **Auto updates** are enabled for `latest_prefer_stable` and `latest` policies. Each deCONZ release does contain the latest official beta and stable signed DDF bundles. These can also be updated by loading fresh ones from the DDF store which doesn't depend on a deCONZ release.

Bundles are assigned according to a policy which is given as a per device `attr/ddf_policy` item.

 Policy              | Description
---------------------|--------------------------------
latest_prefer_stable | **(default)** Use latest DDF bundle: beta signed one if no stable available.
latest               | Use latest DDF bundle either beta or stable signed.
pin                  | Use and stay on bundle given by `<sha256-hash>`.
raw_json             | For development like before bundles existed just use raw .json DDF files.

------------------------------------------------------

## Get all DDF bundle descriptors<a name="getallddfbundledescriptors">&nbsp;</a>

    GET /api/<apikey>/ddf/descriptors[?next=<token>]

Returns the descriptors of all available DDF bundles.

### Parameters

**next** &mdash; The token returned from the last request to query the next descriptors page. The last page requested doesn't specify the next token. The response uses pagination and only returns max N records since in future many thousands of bundles may exist.

### Response
<pre class="headers">
<code class="no-highlight">
HTTP/1.1 200 OK
</code>
</pre>
<pre class="highlight">
<code>
{
   "4273d6eefacefe55ee2e2bc13678206f8237b5e71246ce3cdcaec7a684e3b836":{
      "uuid": "8ecd84ad-4015-4b9e-bee2-311e750ee974",
      "product": "TRÅDFRI bulb E14 WS opal 400lm",
      "version_deconz": ">2.27.0",
      "last_modified": "2024-05-13T10:13:33.000Z",
      "device_identifiers": [
         [
            "IKEA of Sweden",
            "TRADFRI bulb E14 WS opal 400lm"
         ]
      ],
      "file_hash": "fc2ba60cf10d30b4b58fcb70d2eeb5694dda233d07929e1fe5c996b0099e093b"
   },
   "next": 42
}
</code>
</pre>


#### Response fields

The keys in the returned object are the SHA-256 hashes of the immutable data in the DDF bundles (hash over DDFB section).

!!! TODO
    It might be useful to also return the bundle signatures, so a UI can show: official, stable, beta and user labels.
    Since the signatures are made over the SHA-256 hash it's easy to verify them without loading the full bundle.

The **next** key is returned for any but the last response, and if present needs to be specified for the following request to gather the next records.

!!! Note
    The **next** key is an opaque value and likely NOT be incrementally plus 1.
    Thus the first response may return `"next": 24` and the second `"next": 63`.

#### Response fields

<table class="table table-bordered">
  <thead>
    <tr><th>Field</th><th>Type</th><th>Description</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td>uuid</td>
      <td>String</td>
      <td>UUID of the source DDF. It's used to find other version of the DDF on the bundle store.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>product</td>
      <td>String</td>
      <td>Human readable product name.</td>
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
      <td>Timestamp when the bundle sources was last modified.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>device_identifiers</td>
      <td>Array</td>
      <td>Pairs of ZigBee manufacturer name and model id</br>from the Basic cluster.</td>
      <td>R</td>
    </tr>
    <tr>
      <td>file_hash</td>
      <td>String</td>
      <td>SHA256 hash of the file since version 2.27.1</td>
      <td>R</td>
    </tr>
  </tbody>
</table>

### Possible errors

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------

## Get DDF bundle<a name="getddfbundle">&nbsp;</a>

    GET /api/<apikey>/ddf/bundles/<sha256-hash>

### Parameters

None

### Response

The full DDF bundle as *&lt;sha25-hash&gt;.ddf* file.

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
