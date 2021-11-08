# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import subprocess

# p1 = subprocess.run(['D:/kraken/Space_GPS_spoofer/gpssim.exe'], capture_output=True,text=True)
# print(p1.args)
# print(p1.stdout)
# print(p1.stderr)



from ctypes import *

file = "D:/kraken/Space_GPS_spoofer/SDR_lib.so"
fileRun = CDLL(file)

result = fileRun.main("-b","8","-e","brdc3540.14n","-l","30,60,100")

print(result)


