#!/bin/bash
#SCript that shows the content-length from a HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
