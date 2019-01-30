import serial
import time 
ser = serial.Serial('/dev/ttyACM0',115200)  # open serial port
#print(ser.name)         # check which port was really used
j=  -8.5

for i in range(32):

	#print(j)
	jstring = str(j)
	ser.write('U'+str.encode(jstring))     # write a string
	#ser.write(str.encode(jstring))
	print('U'+jstring)
	time.sleep(5)
	##print(ser.read())
	i += 1
	j += 0.5

	

ser.close()             # close port
