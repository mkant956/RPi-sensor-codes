import pwm
import time
i=0
while(True):
	while(i<100):
		#time.sleep(0.01)
		pwm.pwm(23,i)
		i=i+1
	while(i>0):
		#time.sleep(0.01)
		pwm.pwm(23,i)
		i=i-1
	
