# -*- coding: utf-8 -*-
# Modulo que utiliza la API de OpenWeatherMap para devolver información acerce del clima epor ciudades

import json
import urllib
import mtime
from config import get_config

city = get_config.get_config()["ciudad"]

def get_ciudad_from_frase(frase):
  i = 0
  frase = frase.split(" ")
  for palabra in frase:
    if palabra == "en" or palabra == "de":
      return frase[i+1]
    i += 1
    
def traducir_weather(frase):
  return {"mist":"nublado" , "scattered clouds":"nubes dispersas", "broken clouds":"nubes rotas", "clear sky":"cielo claro", "few clouds":"pocas nubes", "shower rain":"aguaceros", "rain":"lluvia", "thunderstorm":"tormenta eléctrica", "drizzle":"llovizna", "sleet":"aguanieve", "clouds":"nublado" }[frase]
    
def get_tiempo_from_frase(frase):
  frase = frase.split(" ")
  dia_actual = mtime.current_day()
  hora_actual = mtime.current_hour()
  
  
def get_clima_actual(frase):
  ciudad = get_ciudad_from_frase(frase)
  if ciudad == None:
    ciudad = city
  direccion = ("http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + "## ID DE LA API ## ")
  response = urllib.urlopen(direccion)
  data = json.loads(response.read())
  estado = traducir_weather(data['weather'][0]['description'])
  return "En la ciudad de " + str(ciudad) + " hoy el clima es " + str(estado) + ". Con una temperatura de entre " + str(data.get('main').get('temp_min')) + " y " + str(data.get('main').get('temp_max')) + str(" grados centígrados.")
  
def get_clima(frase):
  ciudad = get_ciudad_from_frase(frase)
  if ciudad == None:
    ciudad = city
  direccion = ("http://api.openweathermap.org/data/2.5/forecast?q=" + ciudad + "&units=metric&appid=" + " ## APP ID DE LA API ##")
  tiempo =  get_tiempo_from_frase()
  
  return "En la ciudad de " + ciudad + " hoy el clima es " + estado + ". Con una temperatura de entre " + str(data.get('main').get('temp_min')) + " y " + str(data.get('main').get('temp_max')) + str(" grados centígrados.")
