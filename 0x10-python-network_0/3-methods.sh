#!/bin/bash
#script that displays all HTTP methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
