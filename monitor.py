import paho.mqtt.client as paho

fields = {
    "$SYS/broker/clients/connected": "Connected",
    "$SYS/broker/load/messages/received/1min": "Msgs Received",
    "$SYS/broker/publish/messages/dropped": "PUBS DROPPED",
    "$SYS/broker/load/publish/dropped/1min": "LOAD PUBS DROPPED",
    "$SYS/broker/heap/current": "Heap Size",
    "$SYS/broker/heap/maximum": "Heap Max"
}

def on_sub_msg(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload
    prefix = fields[msg.topic]
    fval = float(msg.payload.decode())
    print(f"{prefix} : {msg.payload.decode()}")

if __name__ == '__main__':
    client = paho.Client("monitor")
    client.connect("localhost", 1883)
    for topic in fields:
        client.subscribe(topic)

    client.on_message = on_sub_msg
    client.loop_forever()
    client.disconnect()
