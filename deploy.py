from common import deploy
from itertools import combinations
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
	for iterations in [10000]:
		for size in [64, 1024, 16384]:
			for interval in [5000, 10000]:
				argv = [f"-i {iterations}", f"-m {interval}", f"-s {size}"]

				send_dev_list = ["hc-35", "hc-31", "hc-10"]
				recv_dev_list = ["hc-34", "hc-33", "hc-14"]
				for num in range(len(send_dev_list)):
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
