#!/bin/bash

shopt -s expand_aliases
source ~/.alias

hc kill --devices hc-31 hc-33 hc-34 hc-35 -p wiselab2022
hc start --devices hc-31 hc-33 hc-34 hc-35 -p wiselab2022
