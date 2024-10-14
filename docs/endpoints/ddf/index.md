---
title: Device Description Files (DDF)
---

# Device Description Files (DDF)

!!! Important
    This API is still in development and may change in the future.

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

#### Assignment policies

- **Initial behavior** when a device is joined it is automatically be assigned to a suitable bundle, with priority on the newest bundle that is signed with a "stable" signature and if not found the latest "beta" or unsigned bundle. And if no bundle is found the device will use the raw DDF JSON files or the C++ code as a fallback.

- **Manual update** Once a device is pinned to a bundle, updating to a new DDF bundle version needs to be done explicitly.
  See [Set DDF policy](../devices#put_ddf_policy) page.

- **Auto updates** are enabled for `latest_prefer_stable` and `latest` policies. Each deCONZ release does contain the latest official beta and stable signed DDF bundles. These can also be updated by loading fresh ones from the DDF store which doesn't depend on a deCONZ release.

Bundles are assigned according to a policy which is given as a per device `attr/ddf_policy` item.

 Policy              | Description
---------------------|--------------------------------
latest_prefer_stable | **(default)** Use latest DDF bundle: beta signed one if no stable available.
latest               | Use latest DDF bundle either beta or stable signed.
pin                  | Use and stay on bundle given by `<sha256-hash>`.
raw_json             | For development like before bundles existed just use raw .json DDF files.

------------------------------------------------------

## Create a DDF bundle <a name="createaddfbundle">&nbsp;</a>

There is no dedicated endpoint for creating a DDF bundle, as these are generated from remote sources and signed by the DDF store.

Currently, the DDF store is under development, with plans to introduce a web interface where users can upload and share their bundles. The DDF store already host official DDF bundles.

#### Automatically with the GitHub action

When you submit a pull request that includes a new (or edited) raw DDF JSON file in the `devices` directory,  a GitHub action will automatically generate a temporary DDF bundle. You can view an [example here](https://github.com/dresden-elektronik/deconz-rest-plugin/pull/7900#issuecomment-2307814668). This is helpful for testing the bundle before it is uploaded to the DDF store.

Once the pull request is merged, the new DDF bundle will be uploaded to the bundle store. You can view an [example here](https://deconz-community.github.io/ddf-tools/#/store/bundle/035806b180fcbaf51b143fe2dcd78f2494329000bd02397398a99865bc0127ea).

#### Semi-automatically with the Web-based Auto Bundler

We have introduced a new web-based page to generate DDF bundles. This tool simplifies the bundling process by automating most of the steps. You can access the web-based auto bundler [here](https://deconz-community.github.io/ddf-tools/#/auto-bundler).

Most of the time, the bundler will work seamlessly. However, in some cases, it may prompt you to provide additional files if necessary to complete the bundling process. Follow the on-screen instructions to ensure all required files are included.

#### With the Node.js based bundler

You can also create a DDF bundle manually using the [CLI DDF Tool](https://github.com/deconz-community/ddf-tools/tree/main/packages/cli), which allows you to generate a DDF bundle from a DDF JSON file.

To install the tool, run:
```bash
npm install -g @deconz-community/cli
```

The bundler command generates bundles from the provided DDF JSON source file. Before bundling, ensure the DDFs are valid. Additionally, you'll need to have the [generic directory](https://github.com/dresden-elektronik/deconz-rest-plugin/tree/master/devices/generic), similar to the one found in the `devices` directory of the deCONZ REST plugin repository.

```bash
ddf-tools bundler --help
ddf-tools bundler -o ./output/ devices/ikea/starkvind_air_purifier.json
```

For more details, refer to the [cli tool documentation](https://github.com/deconz-community/ddf-tools/tree/main/packages/cli).

#### With the Community Deconz Toolbox

<mark>In Development</mark>

The [Community Deconz Toolbox](https://deconz-community.github.io/ddf-tools/#/) offers a web interface for creating DDF bundles.

Currently, the toolbox is still under development, with future plans to manage your gateway's DDF bundles and generate new ones.

You can access the bundler by enabling Developer mode in the Settings page.

While the bundler is not yet very user-friendly, it provides an early look at how DDF bundles are created.

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

The full DDF bundle as *&lt;sha25-hash&gt;.ddb* file.

### Possible errors

[403 Forbidden](../../misc/errors#403)

[404 Not Found](../../misc/errors#404)

------------------------------------------------------

## Upload DDF bundle<a name="uploadddfbundle">&nbsp;</a>

    POST /api/<apikey>/ddf/bundles

Uploads a DDF bundle so it can be used by DDF system.

!!! Info
    This endpoint support only one bundle per request but you can use the Phoscon App to upload multiple bundles at once from a zip file.

### Parameters

The DDF bundle is uploaded as `multipart/form-data`, which is used by HTML form input elements with `type="file"` (see: [MSDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition)).

### Example request data

```raw
POST /api/12345/ddf/bundles HTTP/1.1

Content-Type: multipart/form-data;boundary="abcdef"

--abcdef
Content-Disposition: form-data; name="ddfbundle"; filename="example.ddb"

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
[
  {
    "success": {
      "id": "12f39fa2bc4db1990715318e749d6270139609c68fb651a70c59339a91207450"
    }
  }
]
</code>
</pre>

The returned **id** is the DDF bundle SHA-256 hash.

### Possible errors

[400 Bad Request](../../misc/errors#400)

[403 Forbidden](../../misc/errors#403)

------------------------------------------------------
