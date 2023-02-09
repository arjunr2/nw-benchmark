#!/bin/bash

ip link add link eno1 name eno1.5 type vlan id 5 mvrp on egress-qos-map 0:3 1:0 2:1 3:2 4:4 5:5 6:6 7:7
sleep 1
ip addr add 192.168.1.169/24 dev eno1.5
ip link set eno1.5 up
