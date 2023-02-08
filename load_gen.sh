#!/bin/bash

shopt -s expand_aliases
source ~/.alias

#LD_S="hc-31 hc-33 hc-34 hc-35 hc-14 hc-13 hc-11 hc-12 hc-17 hc-18 hc-20" # hc-21 hc-22 hc-23 hc-24 hc-25 hc-26 hc-27"
#LD_R="hc-10"
LD_S="hc-35"
LD_R="hc-33"

set -x
python3 /home/hc/silverline/libsilverline/run.py --config /home/hc/silverline/config.json --path wasm/tests/load_recv.wasm --runtime $LD_R
python3 /home/hc/silverline/libsilverline/run.py --config /home/hc/silverline/config.json --path wasm/tests/load_send.wasm --runtime $LD_S
