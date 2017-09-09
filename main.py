# -*- coding: utf-8 -*-
# Script principal que relaciona el input del STT con el módulo adecuado y envía un output al TTS

from speech import input, output
from modules import mtime, mweather, mcalculator, mwiki, mnoticias, mconversation
from config import change_config, get_config

def search(q):
	
	#if "traducir" in q or "traduce" in q or "traduceme" in q:
        #	return mtranslator.traducir(q)
	
	if "hola" in q or "que tal" in q or "buenos dias" in q or "buenas tardes" in q:
		return mconversation.greet()
	
	elif "adios" in q or "hasta luego" in q or "buenas noches" in q:
		return mconversation.farewell()
	
	elif "hora" in q:
		return mtime.current_time()
		
	elif "clima" in q:
		return mweather.get_clima_actual(q)
	
	elif "operar" in q:
		if "mas" in q:# or "más" in q:
			return mcalculator.sumar(q)
		elif "menos" in q:
			return mcalculator.restar(q)
		elif "por" in q:
			return mcalculator.multiplicar(q)
		elif "entre" in q:
			return mcalculator.dividir(q)
		elif "elevado" in q:
			return mcalculator.potencia(q)
		elif "raiz" in q or "raíz" in q:
			return mcalculator.raiz(q)
		else:
			return "No he entendido la operación, ¿puedes repetirla, por favor?"
	
	elif "que es" in q or "quien es" in q or "quien fue" in q:
		return mwiki.buscar(q)
	
	elif "noticias" in q:
		return mnoticias.get_noticias()
	
	elif "cambiar configuracion" in q:
		return change_config.change_config()

	elif "cambiar" in q and "modo" in q:
		return change_config.change_mode()
	
	else:
		if mconversation.pregunta(q) != 0:
			return mconversation.pregunta(q)
		else:
			return "Perdona, no te he entendido"


while 1:

	if get_config.get_config()["modo"] == "audio":
	        hey = input.ask().lower()
        	while( "hola %s" % (get_config.get_config()["asistente"].lower()) not in hey):
			input.ask().lower()

	#print "beeeep"	
	question = input.ask().lower()
	output.say(search(question))
