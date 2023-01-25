import subprocess
import time
import shlex
import sys
import paho.mqtt.client as paho

'''
    Common helpers for benchmark creation
'''
def construct_deploy (devices, path, argv):
		if type(devices) is str:
				device_str = devices
		else:
				device_str = ' '.join(devices)

		deploy_cmd = "python3 /home/hc/silverline/libsilverline/run.py "\
                 "--config /home/hc/silverline/config.json "\
                f"--path {path} "\
								f"--runtime {device_str} "
		if argv:
				deploy_cmd = deploy_cmd + "--argv {argv}".format(
																argv = ' '.join([f"\"{x}\"" for x in argv]))
		return deploy_cmd

# Return stdout if wait, else return proc instance
def deploy (devices, path, argv=[], wait=True):
    deploy_cmd = construct_deploy (devices, path, argv)
    print(deploy_cmd)
    proc = subprocess.Popen (deploy_cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=sys.stderr,
                            universal_newlines=True)
    if wait:
        stdout, stderr = proc.communicate()
        return stdout

    return proc


'''
    Callback for successful delivery of kill
'''
sync_var = False
def killpub_callback(client, userdata, mid):
    global sync_var
    print("Killing publish threads\n")
    sync_var = True

'''
    Safe killing of all publishers
    Publishes message to 'pubkill'
'''
def kill_pubs (broker_addr, port):
    global sync_var
    client = paho.Client("manager")
    client.connect(broker_addr, port)
    client.on_publish = killpub_callback
    client.loop_start()
    res, mid = client.publish ("pubkill", "kill", qos=1)
    if res:
        raise ValueError("Failure: Publish to pubkill")
    # Wait till kill signal is successfully delivered
    while not sync_var:
        pass
    # Sleep a bit for pub thread to completely kill itself
    time.sleep(0.5)
    client.loop_stop()
    client.disconnect()


