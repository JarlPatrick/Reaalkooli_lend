from pytrack.tracker import *
from time import sleep
import bme280
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

p = GPIO.PWM(25,50)
p.start(7.5)

def openfan():
	p.ChangeDutyCycle(2.5)

def closefan():
	p.ChangeDutyCycle(7.5)

def extra_telemetry():
	tmp,pre,hum = bme280.readBME280All()
	return "{:.2f}".format(tmp) + ',' + "{:.5f}".format(pre) + ',' + "{:.5f}".format(hum)

MT = Tracker()

MT.set_rtty(payload_id='Jarl', frequency=434.250, baud_rate=300)

MT.start()

MT.set_sentence_callback(extra_telemetry)

while True:
	sleep(5)
	openfan()
	sleep(5)
	closefan()
