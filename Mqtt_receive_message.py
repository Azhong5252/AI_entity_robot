import paho.mqtt.client as paho

def Mqtt_receive():
    broker = "broker.hivemq.com"
    NAME = 'unit1'
    mqttmsg = None

    def Mqtt(client, userdata, msg):
        nonlocal mqttmsg
        mqttmsg = str(msg.payload.decode("utf-8"))

    client = paho.Client(NAME)
    client.on_message = Mqtt
    client.connect(broker)
    client.loop_start()
    client.subscribe("playsub")

    while mqttmsg is None:
        pass
    
    client.loop_stop()
    client.disconnect()

    return mqttmsg
