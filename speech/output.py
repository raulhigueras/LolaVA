# -*- coding: utf-8 -*-
# Devuelve la respuesta mediante el TTS de PicoTTS y por el bot de Telegram

import os
import telepot
from config import get_config

bot = telepot.Bot('437025391:AAEjwLO-Mt8jmAQEFjtIikxWR4x8KaB22fI')

def say(respuesta):
	print respuesta
        if get_config.get_profile()["modo"] == "texto":
                bot.sendMessage(get_config.get_ids()["TELEGRAM_CHAT"], respuesta)
	command = 'sudo  pico2wave -w temp/out.wav -l es-ES "' + respuesta +'"'
	os.system(command)
	os.system("aplay temp/out.wav")
