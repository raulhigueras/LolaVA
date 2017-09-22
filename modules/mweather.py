# -*- coding: utf-8 -*-
# Modulo que utiliza la API de OpenWeatherMap para devolver información acerce del clima epor ciudades

import json
import urllib
import mtime
from config import profile, ids

city = profile.get_config()["ciudad"]

def get_ciudad_from_frase(frase):
	i = 0
	frase = frase.split(" ")
	ciudad = []
	en_de = False
	for palabra in frase:
		if en_de:
			ciudad.append(frase[i])
    		if palabra == "en" or palabra == "de":
      			en_de = True	
    		i += 1
	if not ciudad:
		return city
	else:
		return " ".join(ciudad)
    
def api_call(frase):
	ciudad = get_ciudad_from_frase(frase)
        direccion = ("http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&units=metric&appid=" + ids.get_ids()["OPENWEATHERMAP"])
	print direccion
        response = urllib.urlopen(direccion)
        data = json.loads(response.read())
	return data

def traducir_weather(frase):
	return {"mist":"nublado" , "scattered clouds":"nubes dispersas", "broken clouds":"nubes rotas", "clear sky":"cielo claro", "few clouds":"pocas nubes", "shower rain":"aguaceros", "rain":"lluvia", "thunderstorm":"tormenta eléctrica", "drizzle":"llovizna", "sleet":"aguanieve", "clouds":"nublado" }[frase]
  
def get_clima_actual(frase):
	data = api_call(frase) 
	ciudad = get_ciudad_from_frase(frase)
	estado = traducir_weather(data['weather'][0]['description'])
	return "En la ciudad de " + str(ciudad) + " hoy el clima es " + str(estado) + ". Con una temperatura de entre " + str(data['main']['temp_min']) + " y " + str(data['main']['temp_max']) + str(" grados centígrados.")

def get_temperatura_actual(frase):
	data = api_call(frase)
	ciudad = get_ciudad_from_frase(frase)
	return "Hoy la temperatura de "+ str(ciudad) +" ronda en torno a "+ str(data['main']['temp_min']) +" y "+ str(data['main']['temp_max']) +" grados centígrados."

def get_clima(frase):
	ciudad = get_ciudad_from_frase(frase)
	if ciudad == None:
		ciudad = city
  	direccion = ("http://api.openweathermap.org/data/2.5/forecast?q=" + ciudad + "&units=metric&appid=" + ids.get_ids()["OPENWEATHERMAP"])
	tiempo =  get_tiempo_from_frase()
  
  	return "En la ciudad de " + ciudad + " hoy el clima es " + estado + ". Con una temperatura de entre " + str(data.get('main').get('temp_min')) + " y " + str(data.get('main').get('temp_max')) + str(" grados centígrados.")
