import opc
import time
import random

leds = [(255,255,255)]*360 #color white for every pixel

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

for led in range(len(leds)): #picks outs the leds
    leds[led] = (255,0,0)  #making it red
    time.sleep(1)
    client.put_pixels(leds)

led = 0 #to reverse it change to 59
while led<60: #to reverse chaneg it to 'led>=0'
    leds[led] = (0,255,0)
    time.sleep(1)
    client.put_pixels(leds)
    led = led + 1 #'-1' to reverse the order


