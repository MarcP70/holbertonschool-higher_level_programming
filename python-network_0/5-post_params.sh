#!/bin/bash
# This script sends a POST request with parameters and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -L $1
