#!/bin/bash
echo "Building the program publish.cpp"
config-pin p8.16 gpio_pu
g++ publish.cpp -o publish -lpaho-mqtt3c
echo "Finished"
