#!/usr/bin/python
import os
import time
from time import sleep, strftime, time 
import sys
import Adafruit_DHT
import lcddriver


#display = lcddriver.lcd()
with open("data_oficina.csv", "a") as log:

	while True:

   	   humidity, temperature = Adafruit_DHT.read_retry(11, 17)
   	   print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
#   	   display.lcd_display_string("Temperatura: "+str(temperature), 1)
#   	   display.lcd_display_string("Humedad: "+str(humidity), 2)
	   log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temperature),str(humidity)))
           sleep(60)
