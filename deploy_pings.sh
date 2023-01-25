#!/bin/bash

shopt -s expand_aliases
source ~/.alias

cd ../silverline
python3 libsilverline/run.py --config config.json --path wasm/tests/ping_recv.wasm --runtime hc-34
python3 libsilverline/run.py --config config.json --path wasm/tests/ping_send.wasm --argv "-i 1000" --runtime hc-35
