import paho.mqtt.client as paho

broker = "broker.hivemq.com" 
client = ''
NAME = 'unit0'
client = paho.Client(NAME)
client.connect(broker)
client.loop_start()
client.subscribe("playsub")

text = input("請輸入:")
client.publish("playsub", text)
print(text)
