#!/usr/bin/python
from subprocess import Popen
import sys

filename = "/home/pi/lend/test.py"
while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
