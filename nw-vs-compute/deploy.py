from common import deploy
import time
from itertools import combinations, product
import paho.mqtt.client as paho
from argparse import ArgumentParser

sync_var = 0
def on_sub_msg(client, userdata, msg):
    global sync_var
    print(f"Received end of test: {str(msg.payload)}")
    with open(f"{args.type}.results", "ab") as f:
        f.write(msg.payload)
    sync_var = sync_var - 1


def gen_args():
    p = ArgumentParser(description="Kernel deploy nw-vs-compute")
    p.add_argument("--type", "-t", required=True, 
            choices=["local", "offload"], default="local")
    #p.add_argument("--argv", "-a", nargs='*', default=None)
    p.add_argument("--client", "-c", default="hc-20")
    p.add_argument("--server", "-s", default="hc-12")

    return p.parse_args()

def main():
    for n in range(2, 102, 2):
        global sync_var
        sync_var = sync_var + 1
        if args.type == "local":
            deploy(args.client, "wasm/tests/matmul_local.wasm", argv=[n])
        elif args.type == "offload":
            deploy(args.server, "wasm/tests/matmul_offload_kernel.wasm")
            time.sleep(0.4)
            deploy(args.client, "wasm/tests/matmul_offload_client.wasm", argv=[n])
                    
        while sync_var:
            pass

if __name__ == '__main__':
    args = gen_args()
    with open(f"{args.type}.results", "wb") as f:
        pass
    client = paho.Client("manager")
    client.connect("hc-00.arena.andrew.cmu.edu", 1883)
    client.subscribe("test/matmul_res", qos=0)
    client.on_message = on_sub_msg
    client.loop_start()
    main()
    client.loop_stop()
    client.disconnect()
