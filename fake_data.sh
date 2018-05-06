#!/usr/bin/env bash

for i in  $(seq 1 100)
do
    echo
    python /home/naveen/IoT-data-model/device_info.py -d $i
    python /home/naveen/IoT-data-model/device_info.py

done