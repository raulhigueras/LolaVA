import pickle
from speech import output
from speech import input
    
def change_config():
	with open('config/profile.pickle', 'rb') as handle:
		opciones = pickle.load(handle)
    
  	output.say("A continuacion voy a cambiar la configuracion:")
  	output.say("Cual es tu nombre?:")
	opciones["nombre"] = input.ask()
	output.say("Cual es tu periodico favorito?")
	opciones["periodico"] = input.ask()
	output.say("En que ciudad vives?")
	opciones["ciudad"] = input.ask()
	output.say("Cual quieres que sea mi nombre?")
	opciones["asistente"] = input.ask()
  
  	with open('config/profile.pickle', 'wb') as handle:
    		pickle.dump(opciones, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
  	return ("Perfecto, tu nueva configuraciob se ha guardado")
  
def change_mode():
  	with open('config/profile.pickle', 'rb') as handle:
    		opciones = pickle.load(handle)
    
  	if opciones["modo"] == "texto":
    		opciones["modo"] = "audio"
  	else:
    		opciones["modo"] = "texto"

  	with open('config/profile.pickle', 'wb') as handle:
    		pickle.dump(opciones, handle, protocol=pickle.HIGHEST_PROTOCOL)

  	return "El modo se ha cambiado, ahora es: " + opciones["modo"]
