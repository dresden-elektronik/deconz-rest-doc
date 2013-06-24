---
layout: page
title: Polling
nav: misc
---

## Polling state

Since the state of lights and groups might be change from various devices and applications clients shall update their local cache regularly to provide the best user expierience. 

To keep the processing overhead low the API supports the common HTTP `Etag` header to prevent full state updates in each polling attemp.

## Etag HTTP header
