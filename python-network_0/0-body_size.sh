#!/bin/bash
# The script displays the size of the body of the URL request response
echo $(curl -sI $1 | grep Content-Length | awk '{print $2}' | tr -d '\r\n')
