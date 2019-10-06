from math import sqrt
from MCP3008 import MCP3008

ADC_RESOLUTION = 10
ADC_COUNT = 1 << ADC_RESOLUTION

SUPPLY_VOLTAGE = 3.3

class CurrentSensor:

    offsetCurrent = ADC_COUNT >> 1

    def __init__(self, channel, numberOfSamples, callibrationCurrent):
            self.channel = channel
            self.numberOfSamples = numberOfSamples
            self.callibrationCurrent = callibrationCurrent
            self.analogSignal = MCP3008(channel = self.channel)

    def getCurrentSample(self):
        return self.analogSignal.sample()

    def getIrms(self):
        sumCurrent = 0
        
        for i in range(self.numberOfSamples):
            currentSample = self.getCurrentSample()

##            self.offsetCurrent += (currentSample - self.offsetCurrent) / ADC_COUNT
##            filteredCurrent = currentSample - self.offsetCurrent
##
##            sumCurrent += filteredCurrent**2

        currentRatio = self.callibrationCurrent * SUPPLY_VOLTAGE / ADC_COUNT
        return currentRatio * sqrt(sumCurrent / self.numberOfSamples)
        

