#!/bin/bash
#script that sends a JSON POST request to a URL passed as the first argument,
#and displays the body of the response
curl -s "$1" -d "$(cat "$2")" -H "Content-Type: application/json"
