from common import deploy
import time
from itertools import combinations, product
import paho.mqtt.client as paho

sync_var = 0
def on_sub_msg(client, userdata, msg):
    global sync_var
    print("Received end of test")
    sync_var = sync_var - 1


def ping_pair(send_devs, recv_devs, argv, pl_size):
    global sync_var
    num_interf = len(send_devs)
    sync_var = num_interf
    
    # Receive and log deploy
    for i, recv_dev in enumerate(recv_devs):
        deploy(recv_dev, "wasm/tests/ping_recv.wasm", 
                    argv=[f"{send_devs[i]}", f"{pl_size}"], wait=False)
        argvs = argv + [f"-t {send_devs[i]}",  f"-f {num_interf}"]
        deploy(send_devs[i], "wasm/tests/ping_log.wasm", argv=argvs, wait=True)
    time.sleep(0.5)
    # Send deploy
    for send_dev in send_devs:
        argvs = argv + [f"-t {send_dev}",  f"-f {num_interf}"]
        deploy(send_dev, "wasm/tests/ping_send.wasm", argv=argvs, wait=False)
    
    # Wait for sync
    while sync_var:
        pass
    sync_var = 0
	
	
def main():
    iteration_list = [30000]
    size_list = [1024]
    interval_list = [500]
    for iterations, size, interval in product(iteration_list, size_list, interval_list):
        argv = [f"-i {iterations}", f"-m {interval}", f"-s {size}"]

        send_dev_list = ["hc-35", "hc-31", "hc-10"]
        recv_dev_list = ["hc-34", "hc-33", "hc-14"]
        max_num = 1 #len(send_dev_list)
        for num in range(max_num):
            idx = num + 1
            ping_pair(send_dev_list[:idx], recv_dev_list[:idx], argv, size)


if __name__ == '__main__':
    client = paho.Client("manager")
    client.connect("localhost", 1883)
    client.subscribe("test/finish", qos=0)
    client.on_message = on_sub_msg
    client.loop_start()
    main()
    client.loop_stop()
    client.disconnect()
