#!/bin/bash

shopt -s expand_aliases
source ~/.alias

cd ~/silverline/benchmarks
make tests
hc cmd --action put --src wasm/tests/ping_send.wasm --dst wasm/tests/ping_send.wasm
hc cmd --action put --src wasm/tests/ping_recv.wasm --dst wasm/tests/ping_recv.wasm
hc cmd --action put --src wasm/tests/ping_log.wasm --dst wasm/tests/ping_log.wasm
hc cmd --action put --src wasm/tests/load_send.wasm --dst wasm/tests/load_send.wasm
hc cmd --action put --src wasm/tests/load_recv.wasm --dst wasm/tests/load_recv.wasm
hc cmd -x "mkdir -p nw_results"
