# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import subprocess

p1 = subprocess.run(['D:/kraken/Space_GPS_spoofer/gpssim.exe'], capture_output=True,text=True)
print(p1.args)
print(p1.stdout)
print(p1.stderr)