#!/bin/bash

shopt -s expand_aliases
source ~/.alias

hc kill -p wiselab2022
hc start -p wiselab2022
