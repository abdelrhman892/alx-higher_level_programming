#!/bin/bash
# Take in URL, send DELETE request and display response body
curl -sX DELETE "$1"
