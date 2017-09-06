import MCP3202,wiringpi,time,os	# import library WiringPi-Python
from time import sleep                  # import library sleep

wiringpi.wiringPiSetup()		# Must be called before using IO Function
wiringpi.softPwmCreate(4,0,100)		# Set PWM on pin 0, start value 0, max value 100

def translate(value,leftMin,leftMax,rightMin,rightMax):
	# Figure out how 'wide' each range is
    	leftSpan = leftMax - leftMin
    	rightSpan = rightMax - rightMin
    	# Convert the left range into a 0-1 range (float)
    	valueScaled = float(value - leftMin) / float(leftSpan)
    	# Convert the 0-1 range into a value in the right range.
    	return rightMin + (valueScaled * rightSpan)
try:	
 while True :				# endless loop
	os.system('clear')
	value1= MCP3202.readADC(0)	# range data 0 - vref (volt)
	map=translate(value1,0,4096,101,0)
 	print "Proximity Sensor"
	print "Curent Light : ",int(value1),int(map),"%"
    	print ""
	print "Press CTRL+C to exit"
	wiringpi.softPwmWrite(4,int(map))		# PWM pulse on pin 0
	sleep(0.02)                    		# delay for 20ms
	wiringpi.softPwmWrite(4,int(map))		# PWM pulse on pin 0
	sleep(0.02)                    		# delay for 20ms

except KeyboardInterrupt:
	wiringpi.softPwmWrite(4,0)		# PWM pulse on pin 0
	print "exit"	
