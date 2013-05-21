---
layout: page
title: Polling
nav: misc
---

## Polling state

Since the state of lights and groups might be change from various devices and applications clients shall update their local cache regularly to provide the best user expierience. 

To keep the processing overhead low the API supports common HTTP methods like `Etags` and `Last-Modified` headers to prevent full state updates in each polling attemp.

## Etag HTTP header

## Last-Modified HTTP header