# nw-benchmark
Processing and management scripts for end-to-end network benchmarking of Silverline runtime

## Setup
The three modules required for the test are [ping_send.c](https://github.com/SilverLineFramework/benchmarks/blob/master/tests/ping_send.c),
[ping_recv.c](https://github.com/SilverLineFramework/benchmarks/blob/master/tests/ping_recv.c),
[ping_log.c](https://github.com/SilverLineFramework/benchmarks/blob/master/tests/ping_log.c).
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
  - Accepts two arguments: *topic_id* and *payload_size* 
    
### Required Directories
On the machine running `ping_log`, create a directory named `nw_results`
