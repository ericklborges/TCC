# coding=utf-8
from time import time
from time import sleep
from VoltageSensor import VoltageSensor
from CurrentSensor import CurrentSensor

zmpt = VoltageSensor(channel = 0, callibrationVoltage = 845)

sct = CurrentSensor(channel = 1, numberOfSamples = 1480, callibrationCurrent = 91)

count = 0
firstTime = time() * 1000

while True:
    startTime = time() * 1000

    current = sct.getIrms()
    # print("Corrente : %.2f" %(current))
    
    voltage = zmpt.getVrms()
    # print("Tensão: %.2f" %(voltage))

    endTime = time() * 1000
    
    log = open('Logs/log_Circuito_10A.txt', 'a')
    log.write("Amostra: {}\n".format(count))
    log.write("TempoDecorrido: {}ms\n".format(endTime - startTime))
    log.write("TempoTotal: {}ms\n".format(endTime - firstTime))
    log.write("\n")
    log.close()
    
    count += 1

    sleep(0.05)