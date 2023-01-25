#!/bin/bash

shopt -s expand_aliases
source ~/.alias

hc cmd --devices hc-31 hc-33 hc-34 hc-35 hc-10 hc-14 -x "rm -rf nw_results/*"
