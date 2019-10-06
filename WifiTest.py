from random import randint
from urllib import request
from urllib import error
from time import sleep
from time import time
from os import system

led = LED(18)
button = Button(23)

firstTime = time()
failTime = 0
failCount = 0
passedHours = 0

urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "http://dummy.restapiexample.com/api/v1/employee/1",
    "https://api.chew.pro/trbmb",
    "https://uzby.com/api.php?min=3&max=8",
    "https://api.randomuser.me"
    ]
        
def startLedBlinking():
    led.blink(0.5,0.5,None,True)
    
def stopLedBlinking():
    led.on()
    
def startVeryFastLedBlinking():
    led.blink(0.1,0.1,None,True)
        
def run():
    while 1:    
        oneHourInSeconds = 3600
    
        if passedHours == 24:
            log(message = "\nDone")
            startVeryFastLedBlinking()
            break
        elif not(isConnectedToTheInternet()):
            failTime = time()
            failCount += 1
            text = "\n\nDisonnected:{}" 
            log(message = text.format(failCount))
            reconnect()
        elif (time() - firstTime) > oneHourInSeconds:
            passedHours += 1
            text = "\nPassed Hours:{}"
            log(message = text.format(passedHours))
        sleep(30)

def log(message):
    log = open('/home/pi/Git/TCC/Logs/Wifi_Test.txt', 'a')
    log.write(message)
    log.close()

def isConnectedToTheInternet():
    url = urls[randint(0,len(urls)-1)]
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
        elif (time() - startTime) > 120:
            log(message = "timeout")
            reconnect()
        else:
            log(message = '.')
        sleep(0.5)

stopLedBlinking()
button.when_pressed = run

pause()
    
