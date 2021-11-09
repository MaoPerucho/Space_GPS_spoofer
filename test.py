# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import logging
import threading
import time
import subprocess
def print_time(delay):
    count = 0
    while count < 235:
      time.sleep(delay)
      count += 1
      print(count)
      
def thread_function_gpssim():
    p1 = subprocess.run(['D:/kraken/Space_GPS_spoofer/gpssim.exe'], capture_output=True,text=True)
    print(p1.args)
    print(p1.stdout)
    # print(p1.stderr)
    


if __name__ == "__main__":
    x = threading.Thread(target=thread_function_gpssim, args=())
    x.start()
    x = threading.Thread(target=print_time, args=(1,))
    x.start()
    # x.join()