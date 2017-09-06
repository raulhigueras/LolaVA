# -*- coding: utf-8 -*-
# Módulo que utiliza un módulo externo para recoger información de wikipedia
import wikipedia

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
  busqueda = extraer_busqueda_de_frase(frase)
  wikipedia.set_lang("es")
  resumen = wikipedia.summary(busqueda, sentences = 2).encode("utf-8")
  print resumen
  return resumen
