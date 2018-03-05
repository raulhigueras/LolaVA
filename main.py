# -*- encoding: utf-8 -*-
# Script principal que relaciona el input del STT con el módulo adecuado y envía un output al TTS

from speech import input, output
from modules import mtime, mweather, mcalculator, mwiki, mnoticias, mconversation, mrandom, music, mtwitter, mtranslator, mdictionary, mplay
from config import get_config, profile, alarm
import sys, os, time

reload(sys)
sys.setdefaultencoding('utf-8')
reload(sys)

os.system("python subprocess/check_usb.py &")

os.system("aplay resources/sound1.wav")
output.say("Hola, soy Lola. ¿En qué puedo ayudarte?")

def search(q):
		
	if "traducir" in q or "traduce" in q:
       		return mtranslator.traducir(q)

	if "jugar" in q or "juego" in q:
		return mplay.inicio()
	
	if "hola" in q or "buenos dias" in q or "buenas tardes" in q:
		return mconversation.greet()
	
	elif "adios" in q or "hasta luego" in q or "buenas noches" in q:
		return mconversation.farewell()
	
	elif "que hora es" in q:
		return mtime.current_time()
		
	elif ("clima" in q or ("que" in q and "tiempo" in q) or ("como" in q and "tiempo" in q)) and ("manana" in q):
		if ("pasado" in q):
			return mweather.get_clima_actual(q,2)
		else:
			return mweather.get_clima_actual(q,1)
	elif "clima" in q or ("que" in q and "tiempo" in q) or ("como" in q and "tiempo" in q):
		return mweather.get_clima_actual(q,0)
	
	elif ("temperatura" in q or ("hara" in q and "calor" in q) or ("hara" in q and "frio" in q)) and ("manana" in q):
		if ("pasado" in q):
			return mweather.get_temperatura_actual(q,2) 
		else:
			return mweather.get_temperatura_actual(q,1)
	elif "temperatura" in q or ("hace" in q and "calor" in q) or ("hace" in q and "frio" in q):
		return mweather.get_temperatura_actual(q,0)

	elif "calcular" in q or "operar" in q or "cuanto es" in q or "calcula" in q:
		if "mas" in q or "+" in q:
			return mcalculator.sumar(q)
		elif "menos" in q or "-" in q:
			return mcalculator.restar(q)
		elif "por" in q or "x" in q:
			return mcalculator.multiplicar(q)
		elif "entre" in q or "/" in q or ":" in q:
			return mcalculator.dividir(q)
		elif " elevado a " in q or " a la " in q or " al " in q:
			if "cuadrado" in q:
				return mcalculator.potencia(q, 2)
			elif "cubo" in q:
				return mcalculator.potencia(q, 3)
			else:
				try:
					return mcalculator.potencia(q, 0)
				except ValueError:
					return "Lo siento, no he entendido la operación. ¿Podrías repetirla, por favor?"
		elif "raiz" in q:
			if "cuadrada" in q:
				return mcalculator.raiz(q, 2)
			elif "cubica" in q:
				return mcalculator.raiz(q, 3)
			else:
				return mcalculator.raiz(q, 0)
		else:
			return "No he entendido la operación, ¿puedes repetirla, por favor?"

	elif "noticias" in q:
		return mnoticias.get_noticias()
	
	elif "que es" in q or "que son" in q or "quien es" in q or "quien fue" in q or "quien son" in q or "quienes son" in q or "quien fueron" in q or "quienes fueron" in q:
		return mwiki.buscar(q)

	elif "capital de" in q:
		return mwiki.capital(q)
	
	elif "musica" in q:
		return music.music()

	elif "tweet" in q or "tuit" in q or "twittear" in q or "tuitear" in q or "twitter" in q:
		return mtwitter.enviar_tweet()

	elif "tira un dado" in q or "tirar un dado" in q or "lanzar un dado" in q or "lanza un dado" in q:
		return mrandom.dado()
	
	elif "tira una moneda" in q or "tirar una moneda" in q or "lanza una moneda" in q or "lanzar una moneda" in q:
		return random.moneda()

	elif "cambiar configuracion" in q:
		return profile.change_config()

	elif "cambiar" in q and "modo" in q:
		return alarm.change_mode()

	elif "alarma" in q:
		return alarm.change_alarma()
	
	elif "define" in q or "definir" in q or "definas" in q or "definicion" in q:
		return mdictionary.definir(q)

	else:
		if mconversation.pregunta(q) != 0:
			return mconversation.pregunta(q)
		else:
			return "Perdona, no te he entendido."

while 1:
	question = input.ask().lower()
	output.say(search(question))

