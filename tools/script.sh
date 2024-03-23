#!/bin/bash

while IFS=, read -r date latitude longitude measure limit; do
    if [[ "$latitude" == "0" ]]; then
        latitude="0.0"
    fi
    if [[ "$longitude" == "0" ]]; then
        longitude="0.0"
    fi
    echo "$date,$latitude,$longitude,$measure,$limit"
done < DataSet/Speed.csv > Speed.csv