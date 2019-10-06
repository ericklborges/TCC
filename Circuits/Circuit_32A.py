# coding=utf-8
from time import time
from time import sleep
from VoltageSensor import VoltageSensor
from CurrentSensor import CurrentSensor

count = 0
firstTime = time() * 1000

zmpt = VoltageSensor(channel = 4, callibrationVoltage = 845)
sct = CurrentSensor(channel = 5, numberOfSamples = 1480, callibrationCurrent = 91)

while True:
    startTime = time() * 1000

    current = sct.getIrms()
    voltage = zmpt.getVrms()

    endTime = time() * 1000
    
    log = open('/home/pi/Git/TCC/Logs/log_Circuito_32A.txt', 'a')
    log.write("Amostra: {}\n".format(count))
    log.write("TempoDecorrido: {}ms\n".format(endTime - startTime))
    log.write("TempoTotal: {}ms\n".format(endTime - firstTime))
    log.write("\n")
    log.close()
    
    count += 1

    sleep(0.05)