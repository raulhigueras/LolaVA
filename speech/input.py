# -*- coding: utf-8 -*-
# Recoge el input, ya sea mediante el STT de Google o por el bot de Telegram

import speech_recognition as sr

import time, datetime, telepot, os
from config import get_config

bot = telepot.Bot('BOT_KEY')

def ask():
	modo = get_config.get_profile()["modo"]
	os.system("aplay resources/sound2.wav")
	if modo == "texto":
		print "Esperando mensaje"
        	response = bot.getUpdates(offset=-5)
		length = len(response)
		print length
		if(length > 0):
			last_id = response[-1]["update_id"]
			while last_id == bot.getUpdates(offset=-5)[-1]["update_id"]:
                		time.sleep(3)
		else:
			while length == len(response):
				response = bot.getUpdates(offset=-5)
				time.sleep(3)
        	print "---"
        	response =  bot.getUpdates()
		respuesta = clean_input(response[-1]["message"]["text"].lower())
		print respuesta
        	return respuesta
	elif modo == "audio":
		r = sr.Recognizer()
		with sr.Microphone() as source:
			audio = r.listen(source)
	
		try:
			rec = r.recognize_google(audio, language="es-ES")
			print ("Has dicho " + rec)
			return rec.lower()
		except sr.UnknownValueError:
			print( "No se ha entendido el audio")
		except sr.RequestError as e:
			print("Ha habido un error con el reconocimiento de voz {0}".format(e))
	else:
		print "Hay un error con la configuración"

def listen():
	r = sr.Recognizer()
        with sr.Microphone() as source:
        	print("Escuchando")
                audio = r.listen(source)
        try:
                rec = r.recognize_google(audio, language="es-ES")
                if (get_config.get_profile()['asistente'] in rec.lower()):
			return True
		else:
			return False
       	except sr.UnknownValueError:
                print( "No se ha entendido el audio")
        except sr.RequestError as e:
                print("Ha habido un error con el reconocimiento de voz {0}".format(e))

def clean_input(frase):
	caracteres_especiales = {
		'á':'a',
		'é':'e',
		'í':'i',
		'ó':'o',
		'ú':'u',
		'ü':'u',
		'ñ':'n',
		'¿':'?',
		'¡':'!',
	}
	frase = list(frase)
	for i in range(0, len(frase)):
		if caracteres_especiales.has_key(frase[i].encode("utf-8")):
			frase[i] = caracteres_especiales[frase[i].encode("utf-8")]
	if frase[0] == "?" or frase[0] == "!":
		del frase[0]
	if frase[-1] == "?" or frase[-1] == "!":
		del frase[-1]
	return "".join(frase)
