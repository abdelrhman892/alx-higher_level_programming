#!/bin/bash
# Take in URL, send DELETE request, display response body
curl -sX DELETE "$1"
