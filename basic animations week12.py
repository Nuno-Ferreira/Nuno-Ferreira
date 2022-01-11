import opc
import time
import random

leds = [(255,255,255)]*360 #color white for every pixel

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)




