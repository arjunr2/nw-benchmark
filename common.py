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
		print(stdout)
		return stdout
	
	return proc


