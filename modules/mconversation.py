# -*- coding: utf-8 -*-
# Modulo que da respuestas concretas a preguntas concretas, utilizando la informacion de mconversation_res

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
	if hora >= 6 and hora < 12:
		greetings.extend(["¡Buenos dias!", "¿Preparado para empezar el día con energía?"])
		farewells.extend(["¡Qué tengas un buen día!"])
	elif hora >= 12 and hora < 20:
		greetings.extend(["Buenas tardes!", "Que tal esta yendo el dia? Aprovecha que todavia quedan unas horas de sol"])
		farewells.extend(["Adiós, %s. ¡Qué acabes de pasar una buena tarde!" % (nombre)])
	else:
		greetings.extend(["Buenas noches", "Hola de nuevo, " + nombre + ". Espero que hayas tenido un buen dia"])
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

