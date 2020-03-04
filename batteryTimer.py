from time import sleep
from time import strftime
print('Please charge the battery completely.')
print('Transfer power from external source to battery.')
flag = '0'
fileLog = open("batteryTimer.log","w+")
fileLog.close()	
while flag == '0':
	with open("batteryTimer.log","a") as logFile:
		logFile.write("At " + str(strftime("%b %d %Y %H:%M:%S")) + " the computer was on.")
	print('Im still on ' + str(strftime("%b %d %Y %H:%M:%S")) + '.')
	print("\n")
	sleep(300)
	# writes to the file every five minutes when system is on
