# encoding: utf-8 
# Módulo que devuelve mensajes aleatorios

from random import randint

def moneda():
	lado = randint(0,99)
	if lado == 0:
		return "Ha salido canto"
	elif lado % 2 == 0:
		return "Ha salido cara"
	else:
		return "Ha salido cruz"

def dado():
	cara = randint(1,6)
	return "Ha salido "+ str(cara)
