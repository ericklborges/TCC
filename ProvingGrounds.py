import subprocess
from time import sleep

log = open('log.txt', 'a')

for i in range(5):
    log.write("Hello World %d !" %(i))
    log.write("\n")
    
log.close()