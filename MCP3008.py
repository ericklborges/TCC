# Importing modules
import spidev # To communicate with SPI devices
from time import sleep	# To add delay

# Start SPI connection
spi = spidev.SpiDev() # Created an object
spi.open(0,0)

class MCP3008:

    def __init__(self, channel):
        self.channel = channel
        
    # Read MCP3008 data
    def sample(self):
        spi.max_speed_hz = 1350000
        adc = spi.xfer2([1,(8+self.channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
