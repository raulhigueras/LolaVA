# -*- coding: utf-8 -*-
#Módulo relacionado con el tiempo del dispositivo, que principalmente devuelve la hora

import datetime

def current_time():
	ct = datetime.datetime.now()
	return "Son las %s y %s" % (ct.hour, ct.minute)

def current_hour():
	return datetime.datetime.now().hour

def current_day():
	return datetime.datetime.now().day
