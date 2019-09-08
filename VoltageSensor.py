from math import sqrt
from time import time
from time import sleep
from gpiozero import MCP3008

ADC_RESOLUTION = 10
ADC_COUNT = 1 << ADC_RESOLUTION

TIMEOUT = 0.5
CROSSINGS = 20
SUPPLY_VOLTAGE = 3.3

class VoltageSensor:

    firstVoltageSample = 0.0
    offsetVoltage = ADC_COUNT >> 1

    # channel - MCP3008 input channel
    # callibrationVoltage - particular sensor callibration value
    def __init__(self, channel, callibrationVoltage):
            self.channel = channel
            self.callibrationVoltage = callibrationVoltage
            self.analogSignal = MCP3008(channel = self.channel)

    # Calculate Voltage RMS
    def getVrms(self):
        self.firstVoltageSample = self.getInitialVoltageSample()
        return self.calculateVoltageRms()

    # Returns a voltage sample
    def getVoltageSample(self):
        return self.analogSignal.value * 1000.0

    # Returns a voltage sample when
    # waveform is close to zero
    def getInitialVoltageSample(self):

        startTime = time()
        isWaveformCloseToZero = False

        while isWaveformCloseToZero == False:
            voltageSample = self.getVoltageSample()

            timedOut = (time() - startTime) > TIMEOUT
            isBelowUpThreshold = voltageSample < (ADC_COUNT * 0.55)
            isAboveDownThreshold = voltageSample > (ADC_COUNT * 0.45)

            if (isAboveDownThreshold and isBelowUpThreshold) or timedOut:
                isWaveformCloseToZero = True
                return voltageSample

    # Returns Voltage RMS        
    def calculateVoltageRms(self):

        startTime = time()
        crossCount = 0
        sumVoltage = 0.0
        numberOfSamples = 0.0
        
        timedOut = False
        crossedUp = False
        crossedDown = False
        reachedLimitOfCrossings = False

        while (timedOut == False) and (reachedLimitOfCrossings == False):
            voltageSample = self.getVoltageSample()

            self.offsetVoltage += (voltageSample - self.offsetVoltage) / ADC_COUNT
            filteredVoltage = voltageSample - self.offsetVoltage

            sumVoltage += filteredVoltage**2

            if (voltageSample > self.firstVoltageSample):
                crossedDown = False
            else:
                crossedDown = True

            if numberOfSamples == 1 :
                crossedUp = crossedDown

            if crossedUp != crossedDown:
                crossCount += 1

            timedOut = (time() - startTime) > TIMEOUT
            reachedLimitOfCrossings = crossCount >= CROSSINGS
            numberOfSamples += 1

        print("firstVoltageSample: %.2f" %(self.firstVoltageSample))
        print("voltageSample: %.2f" %(voltageSample))
        print("offsetVoltage: %.2f" %(self.offsetVoltage))
        print("filteredVoltage: %.2f" %(filteredVoltage))
        print("sumVoltage: %.2f" %(sumVoltage))
        print("numberOfSamples: %.2f" %(numberOfSamples))
        print("ADC_COUNT: %.2f" %(ADC_COUNT))
        
        voltageRatio = self.callibrationVoltage * SUPPLY_VOLTAGE / ADC_COUNT
        print("voltageRatio: %.2f\n" %(voltageRatio))
        return voltageRatio * sqrt(sumVoltage / numberOfSamples)






        
