#!/bin/bash
# Get the response body for a given URL
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
