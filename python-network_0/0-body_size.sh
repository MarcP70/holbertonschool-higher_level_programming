#!/bin/bash
# The script displays the size of the body of the URL request response

# Take URL as argument
url=$1

# Use curl to send a request and display the size of the body in bytes
size=$(curl -sI $url | grep Content-Length | awk '{print $2}' | tr -d '\r\n')

# Display the size
echo $size
