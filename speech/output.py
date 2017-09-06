# -*- coding: utf-8 -*-
# Devuelve la respuesta mediante el TTS de PicoTTS y por el bot de Telegram

import os
import telepot
from config import get_config, get_ids

bot = telepot.Bot('437025391:AAEjwLO-Mt8jmAQEFjtIikxWR4x8KaB22fI')

def say(respuesta):
	print respuesta
	command = 'sudo  pico2wave -w temp/out.wav -l es-ES "' + respuesta +'"'
	os.system(command)
	os.system("aplay temp/out.wav")
	if get_config.get_config()["modo"] == "texto":
		bot.sendMessage(get_ids.get_ids()["TELEGRAM_CHAT"], respuesta)
