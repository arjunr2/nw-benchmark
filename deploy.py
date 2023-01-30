from common import deploy
from itertools import combinations, product
import paho.mqtt.client as paho

sync_var = 0
def on_sub_msg(client, userdata, msg):
    global sync_var
    print("Received end of test")
    sync_var = sync_var - 1


def ping_pair(send_devs, recv_devs, argv):
    global sync_var
    num_interf = len(send_devs)
    sync_var = num_interf
    
    # Receive deploy
    for i, recv_dev in enumerate(recv_devs):
        deploy(recv_dev, "wasm/tests/ping_recv.wasm", argv=[f"{send_devs[i]}"])
    # Send deploy
    for send_dev in send_devs:
        argvs = argv + [f"-t {send_dev}",  f"-f {num_interf}"]
        deploy(send_dev, "wasm/tests/ping_send.wasm", argv=argvs, wait=False)
    
    # Wait for sync
    while sync_var:
        pass
    sync_var = 0
	
	
def main():
    iteration_list = [10000]
    size_list = [64, 1024, 16384]
    interval_list = [2000, 5000]
    for iterations, size, interval in product(iteration_list, size_list, interval_list):
        argv = [f"-i {iterations}", f"-m {interval}", f"-s {size}"]

        send_dev_list = ["hc-35", "hc-31"]#$, "hc-10"]
        recv_dev_list = ["hc-34", "hc-33"]#, "hc-14"]
        max_num = len(send_dev_list)
        for num in range(max_num):
            idx = num + 1
            ping_pair(send_dev_list[:idx], recv_dev_list[:idx], argv)


if __name__ == '__main__':
    client = paho.Client("manager")
    client.connect("localhost", 1883)
    client.subscribe("test/finish", qos=0)
    client.on_message = on_sub_msg
    client.loop_start()
    main()
    client.loop_stop()
    client.disconnect()
