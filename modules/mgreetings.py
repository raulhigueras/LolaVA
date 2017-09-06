# -*- coding: utf-8 -*-
# Módulo que responde a saludar, eligiendo una respuesta aleatorias entre posibilidades que cambian según la hora del día

import datetime
from random import randint
from config import get_config

nombre = get_config.get_config()["nombre"]

greetings = ["Hola!", "Que tal?", "Cuanto tiempo," + nombre + "!"]

hora = datetime.datetime.now().hour

if hora >= 6 and hora < 12:
  greetings.extend(["Buenos dias!", "Preparado para empezar el dia con energia?", "Hola, " + nombre + " ¡hoy va a ser un gran dia!"])
elif hora >= 12 and hora < 20:
  greetings.extend(["Buenas tardes!", "Que tal esta yendo el dia? Aprovecha que todavia quedan algunas horas de sol"])
else:
  greetings.extend(["Buenas noches", "Hola de nuevo, " + nombre + ". Espero que hayas tenido un buen dia"])
  
def greet():
  return str(greetings[randint(0, len(greetings)-1)])
