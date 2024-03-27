#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and get the size of the response body in bytes
size=$(curl -sI "$1" | awk '/Content-Length/ {print $2}')

# Display the size of the response body in bytes
echo "$size"
