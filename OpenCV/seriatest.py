import serial
import time 
ser = serial.Serial('/dev/ttyACM0',115200)  # open serial port
#print(ser.name)         # check which port was really used

ser.write('U'+str.encode(jstring))     # write a string
time.sleep(5)


	
ser.close()             # close port
