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

## Create a DDF bundle <a name="createaddfbundle">&nbsp;</a>

There is no dedicated endpoint for creating a DDF bundle, as these are generated from remote sources and signed by the DDF store.

Currently, the DDF store is under development, with plans to introduce a web interface where users can upload and share their bundles. The DDF store already host official DDF bundles.

#### Automatically with the GitHub action

When you submit a pull request that includes a new (or edited) raw DDF JSON file in the `devices` directory,  a GitHub action will automatically generate a temporary DDF bundle. You can view an [example here](https://github.com/dresden-elektronik/deconz-rest-plugin/pull/7900#issuecomment-2307814668). This is helpful for testing the bundle before it is uploaded to the DDF store.

Once the pull request is merged, the new DDF bundle will be uploaded to the bundle store. You can view an [example here](https://deconz-community.github.io/ddf-tools/#/store/bundle/035806b180fcbaf51b143fe2dcd78f2494329000bd02397398a99865bc0127ea).

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

**next** &mdash; The token returned from the last request to query the next descriptors. The first and the last request doesn't specify the token. The response uses pagination and only returns max. N records since in future many thousands of bundles may exist.

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
    "uuid": "0737c706-541f-4abb-9c8b-e242b4eeff3a",
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
  },
  "next": 42
}
</code>
</pre>


#### Response fields

The keys in the returned object are the SHA-256 hashes of the immutable data in the DDF bundles (hash over DDFB section).

The **next** key is returned for any but the last response, and if present needs to be specified for the following request to gather the next records.

!!! Note
    The **next** key is an opaque value and likely NOT be incrementally plus 1.
    Thus the first response may return `"next": 24` and the second `"next": 63`.



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
    "uuid": "0737c706-541f-4abb-9c8b-e242b4eeff3a",
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
