# -*- coding: utf-8 -*-
# Módulo que utiliza la libreria googletrans oara traducir palabras o frases

from googletrans import Translator

traductor = Translator()

def extraer_palabra_de_frase(frase):
	traducir = False
	palabra = []
	frase = frase.split(" ")
	for p in frase:
		if traducir == True:
			palabra.append(p)
		if p == "traducir" or p == "traduce":
			traducir = True
	return ' '.join(palabra)

def traducir(frase):
	palabra = extraer_palabra_de_frase(frase)
	resultado = traductor.translate(palabra, dest="es")
	return "La traducción es: " + resultado.text
