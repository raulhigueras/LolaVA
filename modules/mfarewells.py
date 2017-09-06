# -*- coding: utf-8 -*-
# Módulo que responde a despedirse, eligiendo una respuesta eleatoria entre posibilidades que cambian según la hora del día

import datetime
from config import get_config
from random import randint

nombre = get_config.get_config()["nombre"]

farewells = ["Adios!", "Hasta otra!", "Que vaya bien, %s ." % (nombre), "Vale, %s , hablamos luego" % (nombre)]

hora = datetime.datetime.now().hour 

if hora >= 6 and hora < 12:
  farewells.extend(["Que tengas un buen dia!"])
elif hora >= 12 and hora < 20:
  farewells.extend(["Adios, %s. que acabes de pasar bien la tarde!" % (nombre)])
else:
  farewells.extend(["Buenas noches, " + nombre])
  
def farewell():
  return farewells[randint(0, len(farewells)-1)]
