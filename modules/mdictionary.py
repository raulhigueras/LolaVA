# -*- coding: utf-8 -*-
# Módulo que utiliza la API de wikitionary para obtener definiciones

import urllib

def get_palabra_from_frase(frase):
	frase = frase.split(" ")
	palabra = frase[-1]
	return palabra

def definir(frase):
	palabra = get_palabra_from_frase(frase)
	link = "http://www.igrec.ca/project-files/wikparser/wikparser.php?word="+ palabra +"&query=def&lang=es&count=2"
	f = urllib.urlopen(link)
	myfile = f.read()
	separado = myfile.split(" ")
	if(separado[0] == "ERROR:"):
		return "Vaya, parece que esa palabra no está registrado en el diccionario que consulto. ¿Has mirado que esté escrita correctamente?"
	else:
		return myfile

