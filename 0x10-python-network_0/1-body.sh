#!/bin/bash
# Take in URL, send GET request, and display response body

# Check if argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request and capture response
response=$(curl -s "$1")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to fetch URL $1"
    exit 1
fi

# Display the response
echo "$response"
