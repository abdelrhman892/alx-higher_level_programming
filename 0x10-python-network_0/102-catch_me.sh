#!/bin/bash
# that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:You got me!"
