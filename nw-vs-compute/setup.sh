#!/bin/bash

shopt -s expand_aliases
source ~/.alias

cd ~/sl-tests
make
hc-old cmd --devices hc-12 hc-20 -x "mkdir -p wasm/tests"
hc-old cmd --action put --devices hc-12 hc-20 --src wasm/tests/matmul_local.wasm --dst wasm/tests/matmul_local.wasm
hc-old cmd --action put --devices hc-12 hc-20 --src wasm/tests/matmul_offload_kernel.wasm --dst wasm/tests/matmul_offload_kernel.wasm
hc-old cmd --action put --devices hc-12 hc-20 --src wasm/tests/matmul_offload_client.wasm --dst wasm/tests/matmul_offload_client.wasm
