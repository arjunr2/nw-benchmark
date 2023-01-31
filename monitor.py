import paho.mqtt.client as paho

fields = {
    "$SYS/broker/clients/connected": "Connected",
    "$SYS/broker/load/messages/received/1min": "Msgs Received",
    "$SYS/broker/heap/current": "Heap Size"
}

def on_sub_msg(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload
    prefix = fields[msg.topic]
    fval = float(msg.payload.decode())
    print(f"{prefix} : {int(fval)}")

if __name__ == '__main__':
    client = paho.Client("monitor")
    client.connect("localhost", 1883)
    for topic in fields:
        client.subscribe(topic)

    client.on_message = on_sub_msg
    client.loop_forever()
    client.disconnect()
