#encoding: utf-8

import os, time
from speech import input, output
from random import randint
def get_usb():
	path = os.popen("ls /media/pi/").read()
	return path[:-1]

def get_mp3():
	path = get_usb()
	letters = list(os.popen("ls /media/pi/"+path).read())
	files = [[]]
	i = 0
	for l in letters:
	        if l == '\n':
	                i+=1;
	                files.append([])
	        else:
	                files[i].append(l)
	
	files2 = []
	for f in files:
	        if f[-4:] == list(".mp3"):
	                files2.append(''.join(f))
	print files2
	return files2

def music():
	if get_usb() == "":
		return "Ahora mismo no detecto ningún dispositivo USB conectado, vuelve a intentarlo"
	if len(get_mp3()) < 1:
		return "Vaya, parece que tu dispositivo USB no tiene ninguna canción que pueda reconocer. Lo siento"
	path = get_usb()
	output.say("¿Qué quieres que te ponga? Puedes decirme una canción, un artista o aleatorio")
	p = input.ask()
	if (p == "aleatorio" or p == "sorprendeme"):
		num = randint(0, len(get_mp3()))
		song = get_mp3()[num-1]
		output.say("Te estoy poniendo: "+song)
		cmd = "omxplayer /media/pi/"+path+"/'"+song+"'"
		print cmd
		os.system(cmd)
		return "Se acabó"
	else:
		for s in get_mp3():
			if p in s.lower():
				output.say("Perfecto, voy a reproducir "+s)
				os.system("omxplayer /media/pi/"+ path +"/'"+ s + "'")
				return "Se acabó"
		return "No he encontrado ninguna coincidencia con la búsqueda, vuelve a intentarlo"

