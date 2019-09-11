import subprocess
from time import sleep

delay = 0.1

subprocess.Popen(["python", "Circuit_10A.py"])
sleep(delay)

subprocess.Popen(["python", "Circuit_20A.py"])
sleep(delay)

subprocess.Popen(["python", "Circuit_32A.py"])
sleep(delay)