#!/bin/bash

shopt -s expand_aliases
source ~/.alias

cd ~/silverline/benchmarks
make tests
hc cmd --action put --src wasm/tests/ping_send.wasm --dst wasm/tests/ping_send.wasm
hc cmd --action put --src wasm/tests/ping_recv.wasm --dst wasm/tests/ping_recv.wasm
