import subprocess
from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(18)
button = Button(23)

led.blink(0.5,0.5,None,True)

button.when_pressed = led.on

pause()



    