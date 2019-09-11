# coding=utf-8
from time import time
from time import sleep
from VoltageSensor import VoltageSensor
from CurrentSensor import CurrentSensor

zmpt = VoltageSensor(channel = 2, callibrationVoltage = 845)

sct = CurrentSensor(channel = 3, numberOfSamples = 1480, callibrationCurrent = 91)

while True:
    startTime = time()

    print("Circuito 20A")

    current = sct.getIrms()
    print("Corrente : %.2f" %(current))
    
    voltage = zmpt.getVrms()
    print("Tensão: %.2f" %(voltage))

    endTime = time()

    log = open('Logs/log_Circuito_20A.txt', 'a')
    log.write("Tempo Decorrido: %.2fs\n" %(endTime - startTime))
    log.write("\n")
    log.close()
    
    sleep(0.5)
    
