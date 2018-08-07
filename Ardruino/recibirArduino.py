import serial, time, commands, os, string

arduino = serial.Serial('/dev/ttyACM1', 9600)

while 1:
	time.sleep(2)
	texto = arduino.readline()
	try:
		texto = string.atoi(texto)
	except:
		continue

	if texto == 1:
		commands.getoutput('python ./comunicacion.py David')
		
arduino.close()
