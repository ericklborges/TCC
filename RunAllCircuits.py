import subprocess
from gpiozero import LED, Button
from signal import pause
from time import sleep

delay = 0.1
isRunning = false

circuit10AProcess = ""
circuit20AProcess = ""
circuit32AProcess = ""

def toggle():
	if isRunning:
		stop()
	else:
		run()

def run():
	isRunning = true

	circuit10AProcess = subprocess.Popen(["python", "Circuit_10A.py"])
	sleep(delay)

	circuit20AProcess = subprocess.Popen(["python", "Circuit_20A.py"])
	sleep(delay)

	circuit32AProcess = subprocess.Popen(["python", "Circuit_32A.py"])
	sleep(delay)

def stop():
	isRunning = false
	circuit10AProcess.kill()
	circuit20AProcess.kill()
	circuit32AProcess.kill()

led = LED(18)
button = Button(23)

button.when_pressed = toggle

pause()