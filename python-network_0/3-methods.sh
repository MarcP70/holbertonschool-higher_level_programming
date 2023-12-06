#!/bin/bash
# This script send an OPTIONS request and display the allowed methods
echo $(curl -sI -X OPTIONS $1 | grep "Allow" | cut -d ' ' -f 2- | tr -d '\r\n')
