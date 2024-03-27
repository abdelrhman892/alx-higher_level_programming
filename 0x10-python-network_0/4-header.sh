#!/bin/bash
# Take the URL, add header variablea and displays -> Hello School!
curl -s -H "X-School-User-Id":98 "$1"
