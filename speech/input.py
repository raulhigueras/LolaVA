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
	modo = get_config.get_profile()["modo"]
	if modo == "texto":
		print "Esperando mensaje"
        	bot.sendMessage(get_config.get_ids()["TELEGRAM_CHAT"], "Di algo!")
        	response = bot.getUpdates(offset=-5)
        	last_id = response[-1]["update_id"]
		while last_id == bot.getUpdates(offset=-5)[-1]["update_id"]:
                	time.sleep(3)
        	print "---"
        	response =  bot.getUpdates()
        	return response[-1]["message"]["text"].lower()
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
