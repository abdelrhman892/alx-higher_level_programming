#!/bin/bash
# Take the URL and display all methods exits
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
