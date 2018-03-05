#encoding: utf-8
import os, time

while 1==1:
	path = os.popen("ls /media/pi/").read()
	if path == "":
		path = os.popen("ls /media/pi/").read()
	else:
		os.system("aplay subprocess/resources/alarm_sound.wav -d 1")
		while(path != ""):
			path = os.popen("ls /media/pi/").read()
			time.sleep(1)
	time.sleep(1)
