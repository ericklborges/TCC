from gpiozero import LED, Button
from datetime import datetime
from random import randint
from urllib import request
from signal import pause
from urllib import error
from time import sleep
from time import time
from os import system

led = LED(18)
button = Button(23)

firstTime = 0
failTime = 0
failCount = 0
passedHours = 0
lastUsedUrl = ""

urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "http://dummy.restapiexample.com/api/v1/employee/1",
    "https://uzby.com/api.php?min=3&max=8",
    "https://api.randomuser.me",
    "https://uselessfacts.jsph.pl/random.json",
    "https://opinionated-quotes-api.gigalixirapp.com/v1/quotes"
]
        
# Main Loop
def run():
    startDate = datetime.now()
    startDate.strftime("%H:%M:%S")
    text = "\n\n==========\tTest Started at: {}\t==========\n"
    log(message = text.format(startDate.time()))
    global firstTime
    firstTime = time()
    while 1:
        global passedHours
        oneHourInSeconds = 60 * 60
        oneDayInSeconds = oneHourInSeconds * 24
        elapsedTime = time() - firstTime
        stopLedBlinking()
        
        if (elapsedTime / oneHourInSeconds) > (passedHours + 1):
            passedHours += 1
            text = "Passed Hours:{}"
            log(message = text.format(passedHours))
            
        if elapsedTime > oneDayInSeconds:
            startVeryFastLedBlinking()
            endDate = datetime.now()
            endDate.strftime("%H:%M:%S")
            text = "\n\n==========\tTest Ended at: {}\t==========\n"
            log(message = text.format(endDate.time()))
            system("sudo shutdown")
            break
        elif not(isConnectedToTheInternet()):
            global failTime
            failTime = time()
            global failCount
            failCount += 1
            global lastUsedUrl
            failDate = datetime.now()
            failDate.strftime("%H:%M:%S")
            text = "\n\nDisonnected:{}"
            text += "\nTest url:{}"
            text += "\nTime:{}"
            log(message = text.format(failCount,lastUsedUrl,failDate.time()))
            reconnect()   
        sleep(10)

# Log
def log(message):
    log = open('/home/pi/Git/TCC/Logs/Log_Wifi_Test.txt', 'a')
    log.write(message)
    log.close()

# Reachability
def isConnectedToTheInternet():
    global lastUsedUrl
    url = urls[randint(0,len(urls)-1)]
    lastUsedUrl = url
    try:
        request.urlopen(url)
        return True
    except:
        return False

def reconnect():
    startLedBlinking()
    startTime = time()
    system("wpa_cli -i wlan0 reconfigure")
    log(message = "\nreconnecting")
    while 1:
        if isConnectedToTheInternet():
            stopLedBlinking()
            global failTime
            text = "\nReconnection delay:{}"
            log(message = text.format(time() - failTime))
            break
        elif (time() - startTime) > 60:
            log(message = "timeout")
            reconnect()
        else:
            log(message = '.')
        sleep(0.1)

# LED Blinking Patterns
def startLedBlinking():
    led.blink(0.5,0.5,None,True)
    
def stopLedBlinking():
    led.on()
    
def startVeryFastLedBlinking():
    led.blink(0.1,0.1,None,True)

# Main Script
startVeryFastLedBlinking()
button.when_pressed = run

pause()
    

