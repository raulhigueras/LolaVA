# -*- coding: utf-8 -*-
# Configuracion de la alarma 

import pickle, datetime, os 
from speech import input, output

def new_alarma():
        opciones = {
                "hora":datetime.datetime(1900, 1, 1),
                "texto":"",
        }

        with open('config/alarm.pickle', 'wb') as handle:
                pickle.dump(opciones, handle, protocol=pickle.HIGHEST_PROTOCOL)

def get_alarma():
        with open('config/alarm.pickle', 'rb') as handle:
                return pickle.load(handle)

def is_alarma():
	a = get_alarma()
	ring = a['hora']
	hoy = datetime.datetime.now()
	if ring.day < hoy.day or (ring.day == hoy.day and ring.hour < hoy.hour) or (ring.day == hoy.day and ring.hour == hoy.hour and ring.minute < hoy.minute):
		return False
	else:
		return True

def change_alarma():
        opciones = get_alarma()
	if(is_alarma()):
		output.say("Ya hay una alarma programada para las "+str(opciones['hora'].hour)+ " y "+str(opciones['hora'].minute))
		output.say("¿Quieres que la borre y programe una nueva?")
		res = input.ask()
		while(res != "si" and res != "vale" and res != "ok" and res != "no"):
			output.say("Perdona, no te entiendo.¿Quieres que borre la alarma programada y cree una nueva?")
			res = input.ask()
		if res == "no":
			return "Vale, tu alarma no ha sido modificada"
			
	output.say("Voy a configurar tu alarma")
        output.say("¿A qué hora sonará?")
        tiempo = input.ask()
	while(formatearHora(tiempo) == False):
		output.say("Introduce una hora válida, por favor.")
		tiempo = input.ask()
	opciones['hora'] = formatearHora(tiempo)
        output.say("¿Quieres incluir un texto informativo a la alarma?")
        opciones['texto'] = ''
	texto = input.ask()
	while(texto != "si" and texto != "no"):
		output.say("Perdona, no te he entendido. ¿Quieres incluir un texto la alarma?")
		texto = input.ask()
	if texto == "si":
		output.say("Dime qué texto quieres que incluya ")
        	opciones['texto'] = input.ask()	


        with open('config/alarm.pickle', 'wb') as handle:
                pickle.dump(opciones, handle, protocol=pickle.HIGHEST_PROTOCOL)

	os.system("python subprocess/check_alarm.py &")
	now = datetime.datetime.now()
	return "Perfecto, tu alarma sonará en  " + str(opciones["hora"].hour - now.hour) + " horas y " + str(opciones["hora"].minute - now.minute) + " minutos."

def formatearHora(f):
	f = f.split(" ")
	for i in range(0, len(f)):
		if(f[i] == "y"):
			if(f[i+1] == "cuarto"):
				minutos = 15
			elif(f[i+1] == "media"):
				minutos = 30
			else:
				minutos = int(f[i+1])
			hora = int(f[i-1])
		elif(f[i] == "menos"):
			if(f[i+1] == "cuarto"):
				minutos = 45
			else:
				minutos = 60 - int(f[i+1])
			hora = int(f[i-1]) - 1

	hoy = datetime.datetime.now()
	fechahora = datetime.datetime.strptime(str(hora)+":"+ str(minutos)+":00 "+str(hoy.day)+"/"+str(hoy.month)+"/"+str(hoy.year), "%H:%M:%S %d/%m/%Y")
	if(hora < hoy.hour or (hora == hoy.hour and minutos < hoy.minute)):
		fechahora =  fechahora + datetime.timedelta(days=1)
	return fechahora
