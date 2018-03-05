# -*- coding: utf-8 -*-
# Módulo que utiliza un módulo externo para recoger información de wikipedia
import json, urllib
from modules.resources import paisesycapitales

def extraer_busqueda_de_frase(frase):
	que_es = False
	busqueda = []
	frase = frase.split(" ")
	for palabra in frase:
		if que_es == True:
			busqueda.append(palabra)
		if palabra == "es" or palabra == "fue":
			que_es = True
	return ' '.join(busqueda)

def buscar(frase):
	direccion = ("https://es.wikipedia.org/w/api.php?action=query&prop=extracts&titles="+ extraer_busqueda_de_frase(frase).title() +"&exintro=&exsentences=2&explaintext=&redirects=&formatversion=2&format=json")
	response = urllib.urlopen(direccion)
	data = json.loads(response.read())
	try:
		resumen = data["query"]["pages"][0]["extract"]
		return styleResumen(resumen)
	except KeyError:
		return "Vaya, parece que no he encontrado una entrada en Wikipedia con ese nombre, prueba otra búsqueda"

def styleResumen(resumen):
	guardar = True
	guardar2 = True
	resumen = list(resumen)
	respuesta = []
	for c in resumen:

		if(c=="["):
			guardar = False
		elif (c == "("):
			guardar2 = False

		if guardar and guardar2:
			respuesta.append(c)

		if(c == "]"):
			guardar = True
		elif(c==")"):
			guardar2 = True

	return "".join(respuesta)
	

def extraer_pais_de_frase(frase):
        de = False
        busqueda = []
        frase = frase.split(" ")
        for palabra in frase:
                if de == True:
                        busqueda.append(palabra)
                if palabra == "de":
                        de = True
        return ' '.join(busqueda)

def capital(frase):
	pais = extraer_pais_de_frase(frase)
	if paisesycapitales.lista.has_key(pais):
		return "La capital de " + pais.title() + " es " + paisesycapitales.lista[pais].title()
	else:
		return "Vaya, parece que no tengo ese país registrado. ¿Seguro que lo has introducido correctamente?"

