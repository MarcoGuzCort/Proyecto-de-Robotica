#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import time
import serial
import sys
 
# Iniciando conexión serial
arduinoPort = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
texto = sys.argv[1]
 
# Retardo para establecer la conexión serial
time.sleep(1.8) 
arduinoPort.write(texto)
 
# Cerrando puerto serial
arduinoPort.close()
