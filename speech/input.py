# -*- coding: utf-8 -*-
# Recoge el input, ya sea mediante el STT de Google o por el bot de Telegram

import speech_recognition as sr

import time
import random
import datetime
import telepot

from config import get_config

bot = telepot.Bot('437025391:AAEjwLO-Mt8jmAQEFjtIikxWR4x8KaB22fI')

def ask():
	modo = get_config.get_config()["modo"]
	if modo == "texto":
        	bot.sendMessage("## ID DE LA CONVERSACION ##", "Di algo!")
        	response = bot.getUpdates()
        	num = len(response)
        	print response
        	while len(bot.getUpdates()) == num:
                	time.sleep(3)
        	print "Nuevo mensaje"
        	response =  bot.getUpdates()
        	return response[-1]["message"]["text"]
	elif modo == "audio":
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Di algo!")
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
