from common import deploy

if __name__ == '__main__':
	print (deploy("hc-34", "wasm/tests/ping_recv.wasm"))
	print (deploy("hc-35", "wasm/tests/ping_send.wasm", argv=["-i 300"])) 
