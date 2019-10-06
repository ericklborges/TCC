from random import randint
from urllib import request
from urllib import error
from time import sleep
from time import time
from os import system

firstTime = time()
failTime = 0
failCount = 0
passedHours = 0

urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "http://dummy.restapiexample.com/api/v1/employee/1",
    "://api.chew.pro/trbmb",
    "https://uzby.com/api.php?min=3&max=8",
    "https://api.randomuser.me"
    ]

def isConnectedToTheInternet():
    url = urls[randint(0,len(urls)-1)]
    try:
        request.urlopen(url)
        return True
    except:
        return False

def reconnect():
    startTime = time()
    system("wpa_cli -i wlan0 reconfigure")
    print("\nreconnecting", end = '')
    while 1:
        if isConnectedToTheInternet():
            global failTime
            text = "\nReconnection delay:{}"
            print(text.format(time() - failTime))
            break
        elif (time() - startTime) > 120:
            print("timeout")
            reconnect()
        else:
            print('.', end = '')
        sleep(0.5)

while 1:    
    oneHourInSeconds = 3600
    
    if passedHours == 24:
        print("Done")
        break
    elif not(isConnectedToTheInternet()):
        failTime = time()
        failCount += 1
        text = "\nDisonnected:{}" 
        print(text.format(failCount))
        reconnect()
    elif (time() - firstTime) > oneHourInSeconds:
        passedHours += 1
        text = "Passed Hours:{}"
        print(text.format(passedHours))
    sleep(30)
    
    
