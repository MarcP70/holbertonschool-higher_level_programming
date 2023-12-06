#!/bin/bash
# This script send an OPTIONS request and display the allowed methods
echo $(curl -sI $1 | grep "Allow" | awk '{print $2}' | tr -d '\r\n')
