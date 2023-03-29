import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
button=2
button2=4
led=3
gpio.setup(led,gpio.OUT)
gpio.setup(button,gpio.IN)

while True :
    if gpio.input(button)==1:
        gpio.output(led,gpio.HIGH)
    
        
    else:
        gpio.output(led,gpio.LOW)
        

     if gpio.input(button2)==0:
         
         gpio.output(led,gpio.LOW)
    else:
        gpio.output(led,gpio.HIGH)
        
 