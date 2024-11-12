#! /bin/bash

#Check if the user has provided exaclty one argument

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

#Greet the user with their name
echo "Hello, $1"
