#!/bin/bash

shopt -s expand_aliases
source ~/.alias

LD_S=hc-14
LD_R=hc-10

python3 /home/hc/silverline/libsilverline/run.py --config /home/hc/silverline/config.json \
          --path wasm/tests/load_send.wasm --runtime $LD_S
python3 /home/hc/silverline/libsilverline/run.py --config /home/hc/silverline/config.json \
          --path wasm/tests/load_recv.wasm --runtime $LD_R
