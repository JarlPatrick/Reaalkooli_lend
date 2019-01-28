from pytrack.tracker import *
from time import sleep
import bme280

def extra_telemetry():
	tmp,pre,hum = bme280.readBME280All()
	return "{:.2f}".format(tmp) + ',' + "{:.1f}".format(pre) + ',' + "{:.0f}".format(hum)

MT = Tracker()

MT.set_rtty(payload_id='Jarl', frequency=434.250, baud_rate=300)

MT.start()

MT.set_sentence_callback(extra_telemetry)

while True:
	sleep(1)
