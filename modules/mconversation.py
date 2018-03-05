#-*- coding: utf-8 -*-
# Modulo que devuelve respuestas concretas a preguntas concretas

import datetime
from random import randint
from config import profile
from modules import mconversation_res

nombre = profile.get_config()["nombre"]

greetings = mconversation_res.greetings
farewells = mconversation_res.farewells
preguntas = mconversation_res.preguntas
respuestas = mconversation_res.respuestas

hora = datetime.datetime.now().hour
def add_hour():
	print hora
	if hora >= 6 and hora < 12:
		print "mañana"
		greetings.extend(["¡Buenos dias!", "¿Preparado para empezar el día con energía?"])
		farewells.extend(["¡Qué tengas un buen día!"])
	elif hora >= 12 and hora < 20:
		print "tarde"
		greetings.extend(["Buenas tardes!", "Que tal esta yendo el dia? Aprovecha que todavia quedan unas horas de sol"])
		farewells.extend(["Adiós, %s. ¡Qué acabes de pasar una buena tarde!" % (nombre)])
	else:
		print "noche"
		greetings.extend(["Buenas noches", "Hola de nuevo, " + nombre + ". Espero que hayas tenido un buen dia", "¿Pero qué haces todavía levantado a estas horas?"])
		farewells.extend(["Buenas noches, %s" % (nombre)])

def greet():
	add_hour()
	return str(greetings[randint(0, len(greetings)-1)])

def farewell():
	add_hour()
	return str(farewells[randint(0, len(farewells)-1)])

def pregunta(p):
	for i in range(0, len(preguntas)):
		for j in range(0, len(preguntas[i])):
			if preguntas[i][j] in p:
				return respuestas[i][randint(0, len(respuestas[i])-1)]
	return 0
