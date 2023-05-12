# deCONZ REST-API Documentation

This repository holds the sources to build the [deCONZ REST-API Documentation](https://dresden-elektronik.github.io/deconz-rest-doc).

All source files are maintained in the `master` branch.

## Github Pages

The actual documentation can be found at https://dresden-elektronik.github.io/deconz-rest-doc.<br/>
It is hosted via Github pages, with the content of the `gh-pages` branch.

## Contributing

The documentation is build with [MkDocs](https://www.mkdocs.org).
The content it mostly written in Markdown files in the `/docs` directory.

We accept pull requests for the `master` branch.

To edit files locally and review the changes before creating a pull request, you need to:


1. Fork and checkout the `master` branch of this repository;
2. Install MkDocs;
```
cd deconz-rest-doc
source venv/bin/activate
pip install mkdocs
```
3. Start local MkDocs webserver;
```
venv/bin/mkdocs serve
```

4. MkDocs now starts a slim webserver on your local machine;

```
INFO    -  Building documentation... 
INFO    -  Cleaning site directory 
INFO    -  Documentation built in 0.72 seconds 
[I 201120 20:18:17 server:335] Serving on http://127.0.0.1:8000
INFO    -  Serving on http://127.0.0.1:8000
[I 201120 20:18:17 handlers:62] Start watching changes
INFO    -  Start watching changes
[I 201120 20:18:17 handlers:64] Start detecting changes
INFO    -  Start detecting changes

```

5. Open http://127.0.0.1:8000 in your browser to view the documentation output.

**Note:** Since MkDocs supports hot reload changes in Markdown files are updated immediately in the browser.

Once your happy with the edits, create a pull request of the `master` branch :tada:

