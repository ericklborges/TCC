import subprocess
from gpiozero import LED, Button
from signal import pause
from time import sleep

delay = 0.1
isRunning = False

led = LED(18)
button = Button(23)

circuit10AProcess = ""
circuit20AProcess = ""
circuit32AProcess = ""

def toggle():
    if isRunning:
        stop()
    else:
        run()

def run():
    global isRunning
    isRunning = True
    stopLedBlinking()
    
    global circuit10AProcess
    circuit10AProcess = subprocess.Popen(["python", "Circuit_10A.py"])
    sleep(delay)
    
    global circuit20AProcess
    circuit20AProcess = subprocess.Popen(["python", "Circuit_20A.py"])
    sleep(delay)

    global circuit32AProcess
    circuit32AProcess = subprocess.Popen(["python", "Circuit_32A.py"])
    sleep(delay)

def stop():
    global isRunning
    isRunning = False
    startLedBlinking()
    
    global circuit10AProcess
    circuit10AProcess.kill()
    
    global circuit20AProcess
    circuit20AProcess.kill()
    
    global circuit32AProcess
    circuit32AProcess.kill()

def startLedBlinking():
    led.blink(0.5,0.5,None,True)
    
def stopLedBlinking():
    led.on()

startLedBlinking()
button.when_pressed = toggle

pause()