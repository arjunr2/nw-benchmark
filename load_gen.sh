#!/bin/bash

shopt -s expand_aliases
source ~/.alias

LD_S="hc-14 hc-13 hc-16 hc-11 hc-12 hc-17 hc-18"
LD_R="hc-10 hc-16"

set -x
python3 /home/hc/silverline/libsilverline/run.py --config /home/hc/silverline/config.json --path wasm/tests/load_send.wasm --runtime $LD_S
python3 /home/hc/silverline/libsilverline/run.py --config /home/hc/silverline/config.json --path wasm/tests/load_recv.wasm --runtime $LD_R
