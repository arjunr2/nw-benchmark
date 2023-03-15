# nw-benchmark
Processing and management scripts for end-to-end network benchmarking of Silverline runtime

## Setup
The three modules required for the test are [ping_send.c](https://github.com/SilverLineFramework/benchmarks/blob/master/tests/ping_send.c),
[ping_recv.c](https://github.com/SilverLineFramework/benchmarks/blob/master/tests/ping_recv.c),
[ping_log.c](https://github.com/SilverLineFramework/benchmarks/blob/master/tests/ping_log.c). The WASM modules for these tests can be built by running `make tests` in the base [benchmarks](https://github.com/SilverLineFramework/benchmarks) repo.

The sender streams timestamped packets at a certain interval periodicity to the receiver. 
The receiver obtains, adds a tag, and sends the message to the logger. 
The logger uses the tag to verify packet integrity, and prints the time difference from the encoded timestamp.
*Note that this implies the sender and logger must share a common clock. For our purposes, we run both of the same machine*

### Main Parameters
- `ping_send`
  - `-t (string)`: Endpoint of mqtt-topic to use (prepends 'test/ping_send/' to this value)
  - `-m (int)`: Interval time between packets in microseconds (us)
  - `-i (int)`: Number of packets/iterations to send
  - `-s (int)`: Size of the packet payload
- `ping_log` must use the *exact same* arguments as `ping_send`
- `ping_recv`
  - Accepts two arguments: *topic_id* and *payload_size* (prepends 'test/ping_recv/' to topic_id) 
    
### Required Directories
On the machine running `ping_log`, create a directory named `nw_results`

## Example run
The following setup runs the ping test between `hc-33` and `hc-34` for 3000 packets with a interval periodicity of 2 ms and payload size of 1kB.
The topic-id `hc-33` must be consistent on all 
```
<DEPLOY on hc-34> ping_recv.wasm hc-33 1024
<DEPLOY on hc-33> ping_log.wasm -t hc-33 -m 2000 -i 3000 -s 1024
<DEPLOY on hc-33> ping_send.wasm -t hc-33 -m 2000 -i 3000 -s 1024
```
