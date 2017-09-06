# -*- coding: utf-8 -*-
#Módulo que busca noticias recientes del periódico seleccionado en la configuración

from config import get_config

import urllib
import json

def get_noticias():
  periodico = get_config.get_config()['periodico']
  api_key = " ## KEY DE LA API ## "
  if periodico == "el pais":
    link = "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fep00.epimg.net%2Frss%2Felpais%2Fportada.xml&api_key=" + api_key
  elif periodico == "el mundo": 
    link = "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Festaticos.elmundo.es%2Felmundo%2Frss%2Fportada.xml&api_key=" + api_key
  elif periodico == "la vanguardia":
    link = "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.lavanguardia.com%2Fmvc%2Ffeed%2Frss%2Fhome&api_key" + api_key
  elif periodico == "abc":
    link = "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.abc.es%2Frss%2Ffeeds%2FabcPortada.xml&api_key=" + api_key
  else:
    return "Parece que hay un problema con la selección de tu periódico. Prueba a cambiar la configuración"
  response = urllib.urlopen(link)
  data = json.loads(response.read())
  frase = []
  i = 0
  while i < 5:
    frase.append(data['items'][i]['title'])
    i = i+1
  return ", ".join(frase).encode('utf-8')
