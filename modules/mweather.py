# -*- coding: utf-8 -*-
# Modulo que utiliza la API de OpenWeatherMap para devolver información meteorológica

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
			if palabra != "manana" and palabra != "pasado":
				ciudad.append(frase[i])
    		if palabra == "en" or palabra == "de":
      			en_de = True	
    		i += 1
	if not ciudad:
		return city
	else:
		return " ".join(ciudad)
    
def api_call(frase, num):
	ciudad = get_ciudad_from_frase(frase)
	if num == 0:
		direccion = ("http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&units=metric&appid=" + ids.get_ids()["OPENWEATHERMAP"])
	elif num > 0:
		direccion = ("http://api.openweathermap.org/data/2.5/forecast/daily?q=" + ciudad + "&mode=json&units=metric&cnt=14&appid=" + ids.get_ids()["OPENWEATHERMAP"])
	print direccion
        response = urllib.urlopen(direccion)
        data = json.loads(response.read())

	if num > 0:
		try:
			return data['list'][num]
		except KeyError:
			return data
	else:
		return data
def traducir_weather(frase):
	print frase
	traducciones = {"heavy intensity rain":"lluvia de alta intensidad", "overcast clouds":"cielo nublado","light rain":"lluvia ligera", "moderate rain": "lluvia moderada", "sky is clear": "cielo claro", "light snow":"nieve ligera", "mist":"niebla" , "scattered clouds":"nubes dispersas", "broken clouds":"nubes rotas", "clear sky":"cielo claro", "few clouds":"pocas nubes", "shower rain":"aguaceros", "rain":"lluvia", "thunderstorm":"tormenta eléctrica", "drizzle":"llovizna", "sleet":"con aguanieve", "clouds":"nublado", "fog":"niebla" }
	if(traducciones.has_key(frase)):
		return traducciones[frase]
	else:
		return frase

def get_clima_actual(frase, num):
	data = api_call(frase, num)
	ciudad = get_ciudad_from_frase(frase)
	try:
		estado = traducir_weather(data['weather'][0]['description'])
	except KeyError:
		return  "Vaya, parece que no tengo esa ciudad registrada. ¿Seguro que has introducido el nombre correctamente?"
	if num == 0:
		result = "En la ciudad de " + str(ciudad) + " hoy el clima es " + str(estado) + ". Con una temperatura de entre " + str(data['main']['temp_min']) +  " y " + str(data['main']['temp_max']) + str(" grados centígrados.")
	else:
		result = "De aquí a " + str(num) + " días el clima de " + str(ciudad) + " será " + str(estado) + ". Con una temperatura de entre " + str(data['temp']['min']) + " y " + str(data['temp']['max']) + " grados centígrados."
	return result

def get_temperatura_actual(frase, num):
	data = api_call(frase, num)
	ciudad = get_ciudad_from_frase(frase)
	if (num == 0):
		try:
			temp_min = str(data['main']['temp_min'])
		except KeyError:
			return "Vaya, parece que no tengo registrada la ciudad que dices. ¿Seguro que la has escrito bien?"
	else:
		try:
                        temp_min = str(data['temp']['min'])
                except KeyError:
                        return "Vaya, parece que no tengo registrada la ciudad que dices. ¿Seguro que la has escrito bien?"
	if num == 0:
		return "Hoy la temperatura de "+ str(ciudad) +" ronda en torno a "+ str(data['main']['temp_min']) +" y "+ str(data['main']['temp_max']) +" grados centígrados."
	else:
		return "De aquí a " + str(num) + " días la temperatura de " + str(ciudad) + " rondará en torno a " + str(data['temp']['min']) + " y " + str(data['temp']['max']) + " grados centígrados."				

def get_clima(frase):
	ciudad = get_ciudad_from_frase(frase)
	if ciudad == None:
		ciudad = city
	direccion = ("http://api.openweathermap.org/data/2.5/forecast?q=" + ciudad + "&units=metric&appid=" + ids.get_ids()["OPENWEATHERMAP"])
	tiempo = get_tiempo_from_frase()
	
	return "En la ciudad de " + ciudad + " hoy el clima es " + estado + ". Con una temperatura de entre " + str(data.get('main').get('temp_min')) + " y " + str(data.get('main').get('temp_max')) + "grados centígrados."

