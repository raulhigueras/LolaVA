import pickle
from speech import output
from speech import input
    
def change_ids():
	with open('config/ids.pickle', 'rb') as handle:
		ids = pickle.load(handle)
    
  	output.say("A continuacion voy a cambiar las IDs de los servicios que utilizo.")
  	output.say("Id de Rss2Json:")
	ids["RSS2JSON"] = input.ask()
	output.say("Id de Openweathermap:")
	ids["OPENWEATHERMAP"] = input.ask()
	output.say("Id de conversacion con el bot de Telegram:")
	ids["TELEGRAM_CHAT"] = input.ask()
  
  	with open('config/ids.pickle', 'wb') as handle:
    		pickle.dump(ids, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
  	return ("Perfecto, he guardado tus nuevos IDs")

