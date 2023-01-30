#!/bin/bash

shopt -s expand_aliases
source ~/.alias

cd ~/silverline/benchmarks
make tests
hc cmd --devices hc-31 hc-33 hc-34 hc-35 hc-10 hc-14 --action put --src wasm/tests/ping_send.wasm --dst wasm/tests/ping_send.wasm
hc cmd --devices hc-31 hc-33 hc-34 hc-35 hc-10 hc-14 --action put --src wasm/tests/ping_recv.wasm --dst wasm/tests/ping_recv.wasm
hc cmd --devices hc-31 hc-33 hc-34 hc-35 hc-10 hc-14 --action put --src wasm/tests/load_send.wasm --dst wasm/tests/load_send.wasm
hc cmd --devices hc-31 hc-33 hc-34 hc-35 hc-10 hc-14 --action put --src wasm/tests/load_recv.wasm --dst wasm/tests/load_recv.wasm
hc cmd --devices hc-31 hc-33 hc-34 hc-35 hc-10 hc-14 -x "mkdir -p nw_results"
