if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from config import alarm
	from speech import output
    else:
        from ..config import alarm
	from ..speech import output

from os import system
import datetime, time

now = datetime.datetime.now()
alarma = alarm.get_alarma()

while(now.day < alarma['hora'].day or (now.day == alarma['hora'].day and now.hour < alarma['hora'].hour) or (now.day == alarma['hora'].day and now.hour == alarma['hora'].hour and now.minute < alarma['hora'].minute)):
	time.sleep(3)
	now = datetime.datetime.now()

system("aplay subprocess/resources/alarm_sound.wav")

if(alarma['texto'] != ''):
	output.say(alarma['texto'].encode('utf-8'))
