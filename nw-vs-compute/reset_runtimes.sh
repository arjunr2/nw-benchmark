#!/bin/bash

shopt -s expand_aliases
source ~/.alias

hc-old kill --devices hc-20 hc-12 -p wiselab2022
hc-old start --devices hc-20 hc-12 --verbose=0 -p wiselab2022
